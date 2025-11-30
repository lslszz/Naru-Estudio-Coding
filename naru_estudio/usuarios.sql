-- Creación previa de BD "naru_estudio" en SQL en la consola
-- Postgres y del model Usuario en models.py

-- Esto parchea el problema de timestamp que Django no está haciendo
-- en la columna creado_en
ALTER TABLE naruapp_usuario
ALTER COLUMN creado_en SET DEFAULT NOW();

INSERT INTO naruapp_usuario (email, nombre, apellido, rango, rol) VALUES
('camila.munoz@alu.uct.cl', 'Camila', 'Munoz', 'admin', 'supervisor'),
('javier.rojas@mayor.cl', 'Javier', 'Rojas', 'admin', 'supervisor'),
('valentina.diaz@ufrontera.cl', 'Valentina', 'Diaz', 'moderador', 'supervisor'),
('matias.fernandez@mayor.cl', 'Matias', 'Fernandez', 'moderador', 'supervisor'),
('carlos.soto@alu.uct.cl', 'Carlos', 'Soto', 'normal', 'tutor'),
('sofia.torres@ufrontera.cl', 'Sofia', 'Torres', 'normal', 'tutor'),
('andres.araya@mayor.cl', 'Andres', 'Araya', 'normal', 'tutor'),
('fernanda.silva@alu.uct.cl', 'Fernanda', 'Silva', 'normal', 'tutor'),
('diego.perez@ufrontera.cl', 'Diego', 'Perez', 'normal', 'estudiante'),
('ignacia.castillo@mayor.cl', 'Ignacia', 'Castillo', 'normal', 'estudiante'),
('benjamin.morales@alu.uct.cl', 'Benjamin', 'Morales', 'normal', 'estudiante'),
('antonia.vera@ufrontera.cl', 'Antonia', 'Vera', 'normal', 'estudiante'),
('cristobal.mendez@mayor.cl', 'Cristobal', 'Mendez', 'normal', 'estudiante'),
('martina.carrasco@alu.uct.cl', 'Martina', 'Carrasco', 'normal', 'estudiante'),
('sebastian.herrera@ufrontera.cl', 'Sebastian', 'Herrera', 'normal', 'estudiante'),
('isidora.escobar@mayor.cl', 'Isidora', 'Escobar', 'normal', 'estudiante'),
('felipe.rios@alu.uct.cl', 'Felipe', 'Rios', 'normal', 'estudiante'),
('daniela.sandoval@ufrontera.cl', 'Daniela', 'Sandoval', 'normal', 'estudiante'),
('vicente.guzman@mayor.cl', 'Vicente', 'Guzman', 'normal', 'estudiante'),
('trinidad.ojeda@alu.uct.cl', 'Trinidad', 'Ojeda', 'normal', 'estudiante');
