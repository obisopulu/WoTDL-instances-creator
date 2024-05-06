fluidiy()




window.addEventListener("load", () =>{
    fluidiy();
    turnOffSplash()
});

window.addEventListener("resize", () =>{
    fluidiy();
    turnOffSplash()
});

function fluidiy(){
    _('splash').style.width = window.innerWidth + "px";    
    _('splash').style.height = window.innerHeight + "px";
    _('splash1').style.height = (window.innerHeight * 0.4) + "px";
    _('splash2').style.height = (window.innerHeight * 0.6) + "px";
    _('splash2').style.width = _('splash1').style.width = window.innerWidth + "px";
    
    _('bodyTABLE').style.height = window.innerHeight - 100 + "px";
    _('bodyTABLE').style.width = window.innerWidth - 100  + "px"; 
}

function turnOffSplash(){
    //_('splash').style.display = "none"
}

var count
myInterval = setInterval(terminalAutoScroll, 100);
function terminalAutoScroll(){
    _('terminalDIVcontent').scrollTop += 1

    if(_('terminalDIVcontent').scrollTop == count){
        clearInterval(myInterval)
    }
    count = _('terminalDIVcontent').scrollTop;
}



console.log("better days ahead")