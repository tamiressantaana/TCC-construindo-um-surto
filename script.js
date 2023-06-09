function validateEmail(email) {
    const re = /\S+@\S+\.\S+/;
    return re.test(email);
  }

  function handleInputChange(event) {
    const emailInput = event.target;
    const subscribeBtn = document.getElementById("botao-inscricao");

    if (validateEmail(emailInput.value)) {
      subscribeBtn.disabled = false;
    } else {
      subscribeBtn.disabled = true;
    }
  }