let memberSearch=document.getElementById("memberSearch");
let searchBtn=document.getElementById("searchBtn");
let displayMember=document.getElementById("displayMember");
let noResult=document.getElementById("noResult");
let members_data=JSON.parse(document.getElementById("members-data").textContent);


function dataretrive(name){
    if(name===""){
        members_data.forEach(member => {
        displayMember.innerHTML += `
        <tr>
          <td>${member.id}</td>
          <td>${member.name}</td>
          <td>${member.email}</td>
          <td>${member.phone}</td>
          <td>${member.type}</td>
        </tr>
      ` ;
        })
    }
    else{
    members_data.forEach(member => {
        if(member.name.toLowerCase().includes(name)){
            displayMember.innerHTML += `
        <tr>
          <td>${member.id}</td>
          <td>${member.name}</td>
          <td>${member.email}</td>
          <td>${member.phone}</td>
          <td>${member.type}</td>
        </tr>
      ` ;
        }
    
    
    });
}}


searchBtn.addEventListener("click",function(event){
    event.preventDefault();
    displayMember.innerHTML="";
    let name=memberSearch.value.toLowerCase().trim();
    dataretrive(name);
})

