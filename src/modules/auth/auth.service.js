const jwt = require("jsonwebtoken");
const bcrypt = require("bcryptjs");
const { PrismaClient } = require("@prisma/client");
const prisma = new PrismaClient();

const generateToken = (user) => {
  return jwt.sign(
    {
      id: user.id,
      cedula: user.cedula,
      role: user.userType.name,
      status: user.userStatus.name,
    },
    process.env.JWT_SECRET,
    { expiresIn: "2h" }
  );
};

const login = async (cedula, password) => {
  const user = await prisma.user.findUnique({
    where: { cedula },
    include: {
      userType: true,
      userStatus: true,
    },
  });

  if (!user || !(await bcrypt.compare(password, user.password))) {
    throw new Error("Cédula o contraseña inválida");
  }

  if (user.userStatus.name !== "ACTIVE") {
    throw new Error("Tu cuenta no está activa");
  }

  const token = generateToken(user);
  return { user, token };
};

module.exports = { login };

const register = async ({ cedula, password, name, role = 'STAFF' }) => {
  const existingUser = await prisma.user.findUnique({ where: { cedula } });
  if (existingUser) throw new Error("La cédula ya está registrada");

  const hashedPassword = await bcrypt.hash(password, 10);

  const userType = await prisma.userType.findUnique({ where: { name: role.toUpperCase() } });
  const userStatus = await prisma.userStatus.findUnique({ where: { name: 'ACTIVE' } });

  if (!userType || !userStatus) throw new Error("Tipo de usuario o estado inválido");

  const newUser = await prisma.user.create({
    data: {
      cedula,
      password: hashedPassword,
      name,
      userTypeId: userType.id,
      userStatusId: userStatus.id,
    },
    include: {
      userType: true,
      userStatus: true,
    }
  });

  const token = generateToken(newUser);

  return { user: newUser, token };
};

module.exports = { login, register };
