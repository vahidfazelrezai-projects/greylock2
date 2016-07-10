window.onload = function() {
    alert(window.location);
}


window.onclick = function(e){
    e = e || event;
    var from = findParent('a',e.target || e.srcElement);
    if (from){
        /* it's a link, actions here */
        alert(e.target);
    }
}
//find first parent with tagName [tagname]
function findParent(tagname,el){
    if ((el.nodeName || el.tagName).toLowerCase()===tagname.toLowerCase()){
        return el;
    }
    while (el = el.parentNode){
        if ((el.nodeName || el.tagName).toLowerCase()===tagname.toLowerCase()){
            return el;
        }
    }
    return null;
}
