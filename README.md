# odoo_veterinary

### Descripción del módulo

Este módulo de odoo consiste en un gestor de animales de un veterinario, el cual permite dar de alta animales y asignarles incidencias a estes.

### Funcionalidad

El módulo consta de dos modelos 'patients.py' y 'incidents.py'.

Patients, nos permite dar de alta animales indicando sus datos y características tales como: nombre, fecha de nacimiento, raza y especie del animal; además tiene un campo calculado número de incidencias el cual hace un conteo de las incidencas que están relacionadas al animal en cuestión.

Incidents, este modelo relaciona icidencias con los animales que esten dados de alta, consta de un campo Many2one que visualiza que animales estan dados de alta y al seleccionar uno de ellos sea auto rellenarán los campos relativos a la información del animal, especie y raza, para el crear la incidencia deberemos también añadir la fecha en al que ocurrió y la descripción de esta. 

Al añadir una incidencia el número de incidencias del animal al que hace referecia aumentará en 1.

### Interfaz

Cada modelo tiene su propia vista, ambas tienen un vista tree para poder visualizar una lista con la información de cada elemento insertado en los modelos, una vista kanban que muestra la misma información que la vista tree pero de una forma más visual y ordenada y una vista form para introducir la información de los campos de cada modelo.

### Objetivos y mejoras futuras

Objetivos, ampliar el módulo hasta que sea completamente funcional.

Vista a futuro, añadir un modelo de ventas de productos animales, donde se puedan dar de alta nuevos productos y relacionar la venta de dichos productos al animal. Un modelo de cirugías y un modelo de dueños de cada animal.
