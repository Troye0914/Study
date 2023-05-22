function name(ID, word){
    let content = document.getElementById(ID);
    let index = 0;
    letter(index, word, content)
}

function letter(index, word, content) {
    if (index <= word.length) {
        content.value = word.substr(0, index++)
        setTimeout(letter, 250, index, word, content)
    }
}

// function name(ID, word){
//     let content = document.getElementById(ID);
//     let index = 0;
//     window.letter = function() {
//         if (index <= word.length) {
//             content.value = word.substr(0, index++)
//             setTimeout('letter()', 250)
//         }
//     }
//     letter()
// }