const express = require("express");
const router = express.Router();
const { handleLogin, handleLogout, handleRegister } = require("./auth.controller");

/**
 * @swagger
 * /api/auth/login:
 *   post:
 *     summary: Inicia sesión con cédula y contraseña
 *     tags: [Auth]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               cedula:
 *                 type: string
 *               password:
 *                 type: string
 *     responses:
 *       200:
 *         description: Sesión iniciada exitosamente
 *       401:
 *         description: Credenciales incorrectas
 */
router.post("/login", handleLogin);

/**
 * @swagger
 * /api/auth/logout:
 *   post:
 *     summary: Cierra sesión del usuario (solo frontend elimina token)
 *     tags: [Auth]
 *     responses:
 *       200:
 *         description: Sesión cerrada correctamente
 */
router.post("/logout", handleLogout);

/**
 * @swagger
 * /api/auth/register:
 *   post:
 *     summary: Registra un nuevo usuario
 *     tags: [Auth]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               cedula:
 *                 type: string
 *               password:
 *                 type: string
 *               name:
 *                 type: string
 *               role:
 *                 type: string
 *                 enum: [ADMIN, STAFF, DOCTOR]
 *     responses:
 *       201:
 *         description: Usuario registrado exitosamente
 *       400:
 *         description: Error de validación o cédula existente
 */
router.post("/register", handleRegister);

module.exports = router;
