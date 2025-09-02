var acertos = 0;
var perdidos = 0;
var errados = 0;
var saldo = 0;
var intervalo = 2000;
var janela = 2000;
var nivel = 1;
var timer = null;

function carregar() {
    document.getElementById('btnStart').addEventListener("click", start); 
    document.getElementById('gramado').addEventListener("mousedown", marteloBaixo);
    document.getElementById('gramado').addEventListener("mouseup", marteloCima); 
    document.getElementById('buraco0').addEventListener("click", martelada);
    document.getElementById('buraco1').addEventListener("click", martelada);
    document.getElementById('buraco2').addEventListener("click", martelada);
    document.getElementById('buraco3').addEventListener("click", martelada);    
    document.getElementById('buraco4').addEventListener("click", martelada);    
}
    
function sobeToupeira() {
    var buraco = Math.floor(1);//(Math.random() * 5);
    var objBuraco = document.getElementById("buraco" + buraco);
    objBuraco.src = 'images/hole-mole.png';
    timer = setTimeout(tiraToupeira, janela, buraco);
    setTimeout(sobeToupeira, intervalo);
} 

function tiraToupeira(buraco){
    var objBuraco = document.getElementById("buraco" + buraco);
    objBuraco.src = 'images/hole.png';
    perdidos++;
    mostraPontuacao();
}

function mostraPontuacao(){
    mostraPontuacaoDe("acertos", acertos);
    mostraPontuacaoDe("perdidos", perdidos);
    mostraPontuacaoDe("errados", errados);
    saldo = Math.max(acertos - perdidos - errados, 0);
    mostraPontuacaoDe("saldo", saldo);
}

function mostraPontuacaoDe(display, valor){
    let objCentena = document.getElementById(display + "_centena");
    let objDezena = document.getElementById(display + "_dezena");
    let objUnidade = document.getElementById(display + "_unidade");
    
    let centena = parseInt(valor / 100);
    let dezena = parseInt((valor / 10) % 10);
    let unidade = parseInt(valor % 10);

    objCentena.src = 'images/caractere_' + centena + '.gif';
    objCentena.alt = centena;
    objDezena.src = 'images/caractere_' + dezena + '.gif';
    objDezena.alt = dezena;
    objUnidade.src = 'images/caractere_' + unidade + '.gif';
    objUnidade.alt = unidade;
}


function martelada(evento){
    if (evento.target.src.includes('hole-mole')) {
        acertos++;
        evento.target.src = 'images/hole.png';
        clearTimeout(timer);
        aumentarNivel();
    } else {
        errados++;
    }
    mostraPontuacao();
}

function aumentarNivel(){  
    if ((saldo > 0) && (saldo === nivel * 10) && ((saldo % 10) === 0)) {
        intervalo = intervalo - (intervalo / 10);
        janela = janela - (janela / 10);
        nivel++;
        document.getElementById("nivel").textContent = "Nível " + nivel;
    }
}

function marteloBaixo(){
    document.getElementById('gramado').style.cursor = 'url(images/hammerDown.png), default';
}

function marteloCima() {
    document.getElementById('gramado').style.cursor = 'url(images/hammer.png), default';
}

function start(){   
    var botao = document.getElementById("btnStart");
    botao.removeEventListener("click", start);
    botao.disable = true;
    sobeToupeira();
}

onload = carregar;