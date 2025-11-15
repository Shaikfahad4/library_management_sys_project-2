let ReturnBtn=document.getElementById("ReturnBtn");
let returnItem=document.getElementById("returnItem");

returnItem.addEventListener("change",function(){
    let id=returnItem.value;
    ReturnBtn.href=`/delete-return/${id}/`;
})
