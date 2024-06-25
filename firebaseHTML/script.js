import {service} from "./js/datebaseConfig.js"

const endPoint = "/Helena"

// Definindo estrutura do corpo do meu objeto do banco.
var body = {
    
}

// Carregando dados do meu banco
const loadData = () => {
    service.load(endPoint).then( data => {
        body = data;
        // console.log(body);

        const rooms = ['LivingRoom', 'Office', 'PrincipalRoom']
        rooms.forEach(room => {
            getLightsValues(room)
            getTvValues(room)
            setTempValues(room)
        });
    })
}
// Definindo os dados no meu banco.
// service.set(endPoint, body)

// ==================  Colocando os dados no HTML   ==================
const getLightsValues = (idLocal) => {
    let lamp = document.getElementById('lightBulb' + idLocal)
    let lightOn = false;

    switch (idLocal) {
        case 'LivingRoom':
            lightOn = body.livingRoom.principalLight;
            break;
        case 'Office':
            lightOn = body.office.principalLight;
            break;
        case 'PrincipalRoom':
            lightOn = body.principalRoom.principalLight;
            break;
    }

    if(lightOn){ 
        lamp.classList.add("light-on")
    } else {
        lamp.classList.remove("light-on")
    }
}

const getTvValues = (idLocal) => {
    let tv = document.getElementById(idLocal + "Tv")
    let tvOn = false;

    switch (idLocal) {
        case 'LivingRoom':
            tvOn = body.livingRoom.tv;
            break;
        case 'Office':
            tvOn = body.office.tv;
            break;
        case 'PrincipalRoom':
            tvOn = body.principalRoom.tv;
            break;
    }

    if(tvOn){ 
        tv.innerHTML = 'On'
    } else {
        tv.innerHTML = 'OFF'
    }
}

const setTempValues = (idLocal) => {
    const TempElement = document.getElementById(idLocal + "Temp")
    const HumidElement = document.getElementById(idLocal + "Humidity")

    let Hvalue = 0;
    let Tvalue = 0;

    switch (idLocal) {
        case 'LivingRoom':
            Hvalue = body.livingRoom.umid;
            Tvalue = body.livingRoom.temp;
            break;
    
        case 'Office':
            Hvalue = body.office.umid;
            Tvalue = body.office.temp;
            break;
    
        case 'PrincipalRoom':
            Hvalue = body.principalRoom.umid;
            Tvalue = body.principalRoom.temp;
            break;
    
        default:
            break;
    }
    
    TempElement.innerHTML = Tvalue
    HumidElement.innerHTML = Hvalue
}

// ================== Funções de Interação com HTML ==================

const toggleLamp = (idRoom) => {
    const element = document.getElementById("lightBulb" + idRoom);
    element.classList.toggle('light-on');

    switch (idRoom) {
        case "LivingRoom":
            body.livingRoom.principalLight = !body.livingRoom.principalLight;
            service.set(endPoint, body);
            break;
            
        case 'Office' :
            body.office.principalLight = !body.office.principalLight;
            service.set(endPoint, body);
            break;

        case 'PrincipalRoom' :
            body.principalRoom.principalLight = !body.principalRoom.principalLight;
            service.set(endPoint, body);
            break;

        default:
            break;
    }
}

const toggleTv = (idRoom) => {
    const element = document.getElementById(idRoom + "Tv")
    let isOn = false;
    switch (idRoom) {
        case "LivingRoom":
            body.livingRoom.tv = !body.livingRoom.tv;
            isOn = body.livingRoom.tv;
            service.set(endPoint, body);
            break;
            
        case 'Office' :
            body.office.tv = !body.office.tv;
            isOn = body.office.tv;
            service.set(endPoint, body);
            break;

        case 'PrincipalRoom' :
            body.principalRoom.tv = !body.principalRoom.tv;
            isOn = body.principalRoom.tv;
            service.set(endPoint, body);
            break;

        default:
            break;
    }
    if(isOn) {
        element.innerHTML = "ON"
    } else {
        element.innerHTML = "OFF"
    }
}

console.log('script loaded');

//! Adicionando as funções no HTML 

window.toggleLamp = toggleLamp
window.toggleTv = toggleTv

setInterval(() => {
    loadData();
}, 2000);