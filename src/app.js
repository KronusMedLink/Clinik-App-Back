const express = require("express");
const cors = require("cors");
const morgan = require("morgan");

const authRoutes = require("./modules/auth/auth.routes");

const app = express();

// Middlewares globales
app.use(cors());
app.use(morgan("dev"));
app.use(express.json());

// Rutas principales
app.use("/api/auth", authRoutes);

// Swagger 
const setupSwagger = require("../swagger");
setupSwagger(app);

module.exports = app;
