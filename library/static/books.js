let books_data=JSON.parse(document.getElementById("books-data").textContent);
let bookData=document.getElementById("bookData");
let searchBook=document.getElementById("searchBook");
let noresult=document.getElementById("noresult");
let category=document.getElementById("category");
let bookView=document.getElementById("bookView");
let memberView=document.getElementById("memberView");
let checkoutView=document.getElementById("checkoutView");
let reportView=document.getElementById("reportView");
// let status=document.getElementById("status");
// let checkout_data=JSON.parse(document.getElementById("checkout-data").textContent);












function retrivesearchdata(name){
let found=false;
    bookData.innerHTML="";
    if(name===""){
        books_data.forEach(book =>{
            bookData.innerHTML+=`
            <tr>
            <td>${book.title}</td>
            <td>${book.author}</td>
            <td>${book.isbn}</td>
            <td>${book.category}</td>
            <td>${book.status}</td>
            </tr>
            `
            ;
        })
    }
    else{
    
    books_data.forEach(book=>{
        if(book.title.toLowerCase().includes(name) ){
            bookData.innerHTML+=`
            <tr>
            <td>${book.title}</td>
            <td>${book.author}</td>
            <td>${book.isbn}</td>
            <td>${book.category}</td>
            <td>${book.status}</td>
            </tr>
            `
            ;
            found=true;
        }
})
    }
    // if(!found){
    //     noresult.classList.remove("d-none");
    //     bookData.classList.add("d-none");
    //     noresult.textContent="no such result";
    // }
}



searchBook.addEventListener("input",function(event){
        let name=searchBook.value.toLowerCase().trim();
        retrivesearchdata(name)

});

function retrivesearchdatabycategory(){
    let categoryname=category.value;
    let found=false;
    bookData.innerHTML="";
    if(categoryname===""){
        books_data.forEach(book =>{
            bookData.innerHTML+=`
            <tr>
            <td>${book.title}</td>
            <td>${book.author}</td>
            <td>${book.isbn}</td>
            <td>${book.category}</td>
            <td>${book.status}</td>
            </tr>
            `
            ;
        })
    }
    else{
    
    books_data.forEach(book=>{
        if(book.category.toLowerCase().includes(categoryname.toLowerCase()) ){
            bookData.innerHTML+=`
            <tr>
            <td>${book.title}</td>
            <td>${book.author}</td>
            <td>${book.isbn}</td>
            <td>${book.category}</td>
            <td>${book.status}</td>
            </tr>
            `
            ;
            found=true;
        }
})
    }
}


category.addEventListener("input",retrivesearchdatabycategory)
category.addEventListener("change",retrivesearchdatabycategory)


