const registerButton = document.getElementById('register');
const loginButton = document.getElementById('login');
const container = document.getElementById('container');

const loginForm = document.getElementById('loginForm');
const loginError = document.getElementById('loginError');

const registerForm = document.getElementById('registerForm');
const registerError = document.getElementById('registerError');

registerButton.addEventListener('click', () => {
    container.classList.add("right-panel-active");
});

loginButton.addEventListener('click', () => {
    container.classList.remove("right-panel-active");
});

loginForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const email = loginForm.querySelector('input[placeholder="Email"]').value;
    const password = loginForm.querySelector('input[placeholder="Password"]').value;


    if (!email || !password) {
        loginError.style.display = 'block';
    } else {
        loginError.style.display = 'none';
        console.log('Form submitted successfully!');
    }
});

registerForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const email = registerForm.querySelector('input[placeholder="Email"]').value;
    const password = registerForm.querySelector('input[placeholder="Password"]').value;
    const name = registerForm.querySelector('input[placeholder="Name"]').value;


    if (!email || !password || !name) {
        registerError.style.display = 'block';
    } else {
        registerError.style.display = 'none'; 
        console.log('Form submitted successfully!');
    }
});
