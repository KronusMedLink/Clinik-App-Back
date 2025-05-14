const { login, register } = require("./auth.service");

const handleLogin = async (req, res) => {
  const { cedula, password } = req.body;

  try {
    const { user, token } = await login(cedula, password);
    res.json({ token, user: { id: user.id, name: user.name, role: user.userType.name } });
  } catch (err) {
    res.status(401).json({ error: err.message });
  }
};

const handleLogout = (req, res) => {
  // Para JWT stateless, el frontend simplemente borra el token.
  res.status(200).json({ message: "Sesión cerrada correctamente" });
};

const handleRegister = async (req, res) => {
  const { cedula, password, name, role } = req.body;

  try {
    const { user, token } = await register({ cedula, password, name, role });
    res.status(201).json({
      token,
      user: {
        id: user.id,
        name: user.name,
        cedula: user.cedula,
        role: user.userType.name,
      }
    });
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

module.exports = { handleLogin, handleLogout, handleRegister };
