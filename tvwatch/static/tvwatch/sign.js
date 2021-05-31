//select element function
const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const sign_container = document.getElementById('sign_container');

//switching cover
signUpButton.addEventListener('click', () => 
sign_container.classList.add('right-panel-active'));

signInButton.addEventListener('click', () => 
sign_container.classList.remove('right-panel-active'));