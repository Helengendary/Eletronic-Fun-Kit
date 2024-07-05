import {service} from "./js/datebaseConfig.js"

const endPoint = "/Mariana"

var body = {
    
}

const loadData = () => {
    service.load(endPoint).then( data => {
        body = data;

        setValues()
    
    })
}

const setValues = () => {
    // const TempElement = 
    // const HumidElement = 

    let Umidade_value = 0;
    let Temperatura_value = 0;
    let Passos_value = 0;
    let Batimentos_value = 0;
    let Oxigenio_value = 0;
    let Horario_value = " ";
    let Semana_value = " ";
    let Dia_value = 0;
    let Mes_value = " ";

    Umidade_value = body.Umidade;
    Temperatura_value = body.Temperatura;
    Passos_value = body.Passos;
    Batimentos_value = body.Batimentos;
    Oxigenio_value = body.Oxigenio;
    Horario_value = body.Horario;
    Semana_value = body.Semana;
    Dia_value = body.Dia;
    Mes_value = body.Mes;
    
    document.getElementById("Temp").innerHTML = Temperatura_value + "°C"
    document.getElementById("Humid").innerHTML = Umidade_value + "%"
    document.getElementById("Hora").innerHTML = Horario_value
    document.getElementById("Data").innerHTML = Semana_value + ", " + Dia_value + " de " + Mes_value
    document.getElementById("passo").innerHTML = Passos_value
    document.getElementById("bpm").innerHTML = Batimentos_value + "bpm"
    document.getElementById("o2").innerHTML = Oxigenio_value + "%"
}

setInterval(() => {
    loadData();
}, 1000);