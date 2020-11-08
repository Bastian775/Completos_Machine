$(document).ready(function(){
    $("#formulario").validate(
    {
        errorClass:'is-invalid',
        rules:{
            nombre:{
                required:true    
            },
            usuario:{
                required:true
            },
            correo:{
                required:true
            },
            pass:{
                required:true
            },
            pass2:{
                required:true
            }
        },
        messages:{
            nombre:{
                required:"Debe ingresar su nombre"    
            },
            usuario:{
                required:"Debe ingresar un nombre de usuario"
            },
            correo:{
                required:"Debe ingresar su correo",
                email:"Debe ingresar un correo valido"
            },
            pass:{
                required:"Debe ingresar una contraseña valida"
            }
        }
    }
    )
})