var nowDetail = null;
var showText = document.getElementById('show-option')
var socials = {
    instagram: 'urfavtrwn3',
    discord: 'Tarantino#8922',
    telegram: '@tariyane',
    number: 'you dont have permission for this'
}
let canShow = true;

function closeALLCollapses(c){
    const collapses = ['col-contact', 'col-about']
    showText.style.display ='none'
    for (let i=0;i < collapses.length;i++){
        document.getElementById(collapses[i]).style.display = 'none'
    }
}
function inCollapse(collapse){
    closeALLCollapses(collapse)
    const COL = document.getElementById(collapse)
    if (nowDetail == collapse){
        COL.style.display = 'none'
        nowDetail = null
    }else{
        COL.style.display = 'flex'
        nowDetail = collapse
    }

}

function inOption(option){
    const OP = document.getElementById(option)
    showText.style.display ='flex'

    const text = socials[option]
    
    if(canShow){
        showText.innerHTML =''
    let i = 0
    var animaP = setInterval(()=>{
        canShow = false
        showText.innerHTML += text[i]
        i++
        if (i == text.length){
            clearInterval(animaP)
            canShow = true
        }
    },50)

    }
}