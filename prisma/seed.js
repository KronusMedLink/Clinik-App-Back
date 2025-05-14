const { PrismaClient } = require('@prisma/client');
const prisma = new PrismaClient();

async function main() {
  // Insertar tipos de usuario
  await prisma.userType.createMany({
    data: [
      { name: 'ADMIN' },
      { name: 'STAFF' },
      { name: 'DOCTOR' },
    ],
    skipDuplicates: true,
  });

  // Insertar estados de usuario
  await prisma.userStatus.createMany({
    data: [
      { name: 'ACTIVE' },
      { name: 'INACTIVE' },
    ],
    skipDuplicates: true,
  });

  console.log("Seed ejecutado correctamente");
}

main()
  .then(() => prisma.$disconnect())
  .catch((e) => {
    console.error(e);
    prisma.$disconnect();
    process.exit(1);
  });
