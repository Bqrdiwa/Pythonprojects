


function Like(albumId){
    let liked = false;
    const filler = document.getElementById(`filler-like-${albumId}`);
    const likeBtn = document.getElementById(`like-btn-${albumId}`);

    if (filler.style.fill =='#C71717'){
        liked = true;
    };

    if (liked == true){
        filler.style.fill = 'white'
    }else{
        filler.style.fill = '#C71717'
    };
    
}


const ADDBTN = document.getElementById('add')
function ADD(){
    ADDBTN.style.transform = 'rotate(90deg)'
    setTimeout(function(){
        ADDBTN.style.transform = 'rotate(0deg)'
        setTimeout(function(){
            window.location.href = '/albumADD/'
        },450)

    },1000)

}