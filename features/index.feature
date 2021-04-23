# language: es

Característica: índice

  Escenario: cargar pagina inicial
      Dado hemos accedido a la aplicación
      Cuando carguemos la pagina /
      Entonces aparece el título "Tienda de Libros"

  Esquema del escenario: libros presentes
      Dado hemos accedido a la aplicación
      Cuando carguemos la pagina /
      Entonces aparece el libro <libro>
   
    Ejemplos: libros
      | libro      | autor               |
      | Hamlet     | William Shakespeare |
      | El Quijote de la Mancha | Miguel de Cervantes |


