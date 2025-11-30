-- Creación previa de BD "naru_estudio" en SQL en la consola Postgres

CREATE TABLE usuarios (
    email VARCHAR(255) UNIQUE NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,

    rango VARCHAR(20) NOT NULL CHECK (
        rango IN ('admin', 'moderador', 'normal')
    ),

    rol VARCHAR(20) NOT NULL CHECK (
        rol IN ('supervisor', 'tutor', 'estudiante')
    ),

    creado_en TIMESTAMP DEFAULT NOW(),

    PRIMARY KEY (email)
);

INSERT INTO usuarios (email, nombre, apellido, rango, rol) VALUES
('camila.munoz@alu.uct.cl', 'Camila', 'Muñoz', 'admin', 'supervisor'),
('javier.rojas@mayor.cl', 'Javier', 'Rojas', 'admin', 'supervisor'),
('valentina.diaz@ufrontera.cl', 'Valentina', 'Díaz', 'moderador', 'supervisor'),
('matias.fernandez@mayor.cl', 'Matías', 'Fernández', 'moderador', 'supervisor'),
('carlos.soto@alu.uct.cl', 'Carlos', 'Soto', 'normal', 'tutor'),
('sofia.torres@ufrontera.cl', 'Sofía', 'Torres', 'normal', 'tutor'),
('andres.araya@mayor.cl', 'Andrés', 'Araya', 'normal', 'tutor'),
('fernanda.silva@alu.uct.cl', 'Fernanda', 'Silva', 'normal', 'tutor'),
('diego.perez@ufrontera.cl', 'Diego', 'Pérez', 'normal', 'estudiante'),
('ignacia.castillo@mayor.cl', 'Ignacia', 'Castillo', 'normal', 'estudiante'),
('benjamin.morales@alu.uct.cl', 'Benjamín', 'Morales', 'normal', 'estudiante'),
('antonia.vera@ufrontera.cl', 'Antonia', 'Vera', 'normal', 'estudiante'),
('cristobal.mendez@mayor.cl', 'Cristóbal', 'Méndez', 'normal', 'estudiante'),
('martina.carrasco@alu.uct.cl', 'Martina', 'Carrasco', 'normal', 'estudiante'),
('sebastian.herrera@ufrontera.cl', 'Sebastián', 'Herrera', 'normal', 'estudiante'),
('isidora.escobar@mayor.cl', 'Isidora', 'Escobar', 'normal', 'estudiante'),
('felipe.rios@alu.uct.cl', 'Felipe', 'Ríos', 'normal', 'estudiante'),
('daniela.sandoval@ufrontera.cl', 'Daniela', 'Sandoval', 'normal', 'estudiante'),
('vicente.guzman@mayor.cl', 'Vicente', 'Guzmán', 'normal', 'estudiante'),
('trinidad.ojeda@alu.uct.cl', 'Trinidad', 'Ojeda', 'normal', 'estudiante');
