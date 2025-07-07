

const myForm = document.getElementById("contactus_form_1")

const formElements = myForm.elements;


const dobField = document.getElementById('dob')


console.log(dob);


const success_message_container = document.getElementById('pop_up_container')
const form_container = document.getElementById("form_container_id")
// myForm.addEventListener('submit', function(event) {
//         // Prevent the default form submission behavior (page reload)
//         event.preventDefault();

//         // Your code to handle form submission goes here
//         console.log('Form submitted!');

//         // You can access form data here
//          const formData = new FormData(event.target);




         
//          console.log(formData.get('name'));
//          let input_name = formData.get('name')

//          success_message_container.style.display = "block"
    
     
//          document.getElementById('pop_up_name').innerText = input_name


//         document.body.style.backgroundColor = "black";
 
//     }     
//     );

    // const closeBtn = document.getElementById("close_btn")

    // closeBtn.addEventListener('click' ,()=>{

    //       myForm.reset();
    //     success_message_container.style.display = "none"
        


    // })

// console.log(" html form",form)


document.getElementById('phnum').addEventListener('change' ,()=>{
    let number = document.getElementById("phnum").value

    const numberAsstring = number+''
    if(numberAsstring.length == 10){
         document.getElementById('invalidnumId').style.display = 'none'
    }
    else{

        document.getElementById('invalidnumId').style.display = 'block'
        number = document.getElementById("phnum").value = ''
    }
})




dobField.addEventListener('change', function() {

        const dob =  document.getElementById('dob').value
        console.log(dob);

        const today = new Date();
        const dob_to_calc = new Date(dob); 

        let age = today.getFullYear() - dob_to_calc.getFullYear();
        const monthDifference = today.getMonth() - dob_to_calc.getMonth();

     
        document.getElementById('age').value = age;
        
    });


// to handle the image 
document.getElementById('imageUpload').addEventListener('change', function () {
            let file = this.files[0];
            let reader = new FileReader();

            reader.onload = function (event) {
                let base64String = event.target.result;
                document.getElementById('preview').src = base64String;
                // document.getElementById('basestring').value = base64String

                document.getElementById('preview').style.display = 'block';
                console.log(base64String);
            };

            reader.readAsDataURL(file);
        });

  console.log(document.getElementById('imageUpload').value);


dob.max = new Date().toLocaleDateString('fr-ca') 

function validateFileType(){
            var fileName = document.getElementById("imageUpload").value,
                idxDot = fileName.lastIndexOf(".") + 1,
                extFile = fileName.substr(idxDot, fileName.length).toLowerCase();
            if (extFile=="jpg" || extFile=="jpeg" || extFile=="png"){
                document.getElementById("imageInvalid").style.display="none"
            }else{
                var fileName = document.getElementById("imageUpload").value = ""
                document.getElementById("imageInvalid").style.display="block"
            }
        }



document.getElementById('imageUpload').addEventListener('change' , validateFileType) 








