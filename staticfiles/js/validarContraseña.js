function validarformulario(){

    var username, password;
    username =document.getElementById('username').value;
    password=document.getElementById('password').value
    
    expresion= /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i;
    
    if ( username ==="" || password==="" ) { 
       error.html(<span>'Todos los campos son obligatorios'</span>);
              return false
    }
    else if (!expresion.test(username.value)){ 
          error.html('<span>Please enter a valid username address</span>');
           return false
         }
    }