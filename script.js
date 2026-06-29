function calcularIMC() {
    const pesoInput = document.getElementById('peso').value;
    const alturaInput = document.getElementById('altura').value;
    const genero = document.getElementById('genero').value;
    
    const txtValor = document.getElementById('imc-valor');
    const txtClassificacao = document.getElementById('imc-classificacao');
    const txtDica = document.getElementById('imc-dica');
    const barraProgresso = document.getElementById('imc-barra');
    const boxResultado = document.getElementById('resultado');

    if (!pesoInput || !alturaInput) {
        alert("Por favor, preencha todos os campos!");
        return;
    }

    let peso = parseFloat(pesoInput);
    let altura = parseFloat(alturaInput);

    if (peso <= 0) {
        alert("Erro: O peso deve ser maior que zero.");
        return;
    }

    if (altura < 0.5 || altura > 3.0) {
        alert("Erro: A altura deve estar entre 0.5 metros e 3.0 metros (somente em metros, sem conversão automática). Exemplo: 1.75");
        return;
    }

    const imc = peso / (altura * altura);
    let classificacao = "";

    if (imc < 16.0) {
        classificacao = "Magreza Grave (Grau III)";
    } else if (imc >= 16.0 && imc < 17.0) {
        classificacao = "Magreza Moderada (Grau II)";
    } else if (imc >= 17.0 && imc < 18.5) {
        classificacao = "Magreza Leve (Grau I)";
    } else if (imc >= 18.5 && imc < 22.0) {
        classificacao = "Peso Normal (Faixa de Transição Baixa)";
    } else if (imc >= 22.0 && imc < 25.0) {
        classificacao = "Peso Normal / Ideal (Parabéns!)";
    } else if (imc >= 25.0 && imc < 27.5) {
        classificacao = "Sobrepeso Inicial (Alerta Leve)";
    } else if (imc >= 27.5 && imc < 30.0) {
        classificacao = "Sobrepeso Avançado (Pré-Obesidade)";
    } else if (imc >= 30.0 && imc < 35.0) {
        classificacao = "Obesidade Grau I (Moderada)";
    } else if (imc >= 35.0 && imc < 40.0) {
        classificacao = "Obesidade Grau II (Severa)";
    } else {
        classificacao = "Obesidade Grau III (Mórbida)";
    }

    // 1. Atualiza Textos Principais
    txtValor.innerText = `IMC: ${imc.toFixed(2)}`;
    txtClassificacao.innerText = `Classificação: ${classificacao}`;

    // 2. Cálculo de Peso Ideal com base no Gênero (Margens OMS adaptadas)
    let pesoMin, pesoMax;
    if (genero === "feminino") {
        pesoMin = (19 * (altura * altura)).toFixed(1);
        pesoMax = (24 * (altura * altura)).toFixed(1);
    } else {
        pesoMin = (20 * (altura * altura)).toFixed(1);
        pesoMax = (25 * (altura * altura)).toFixed(1);
    }
    txtDica.innerHTML = `Para sua altura e gênero, o peso ideal recomendado fica entre <strong>${pesoMin}kg</strong> e <strong>${pesoMax}kg</strong>.`;

    // 3. Atualiza a Barra de Progresso Visual
    // Limitamos o valor exibido na barra entre 15 e 40 para ficar visualmente centrado
    barraProgresso.value = Math.min(Math.max(imc, 15), 40);

    // 4. Aplica Cores Dinâmicas
    boxResultado.classList.remove('hidden', 'status-verde', 'status-amarelo', 'status-vermelho');

    if (imc >= 18.5 && imc < 25.0) {
        boxResultado.classList.add('status-verde');
    } else if ((imc >= 25.0 && imc < 30.0) || (imc >= 17.0 && imc < 18.5)) {
        boxResultado.classList.add('status-amarelo');
    } else {
        boxResultado.classList.add('status-vermelho');
    }
}