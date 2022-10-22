var table = document.getElementById("table"),rIndex;

for(var i=1;i<table.rows.length;i++){
    table.rows[i].onclick = function(){
        rIndex = this.rowIndex;
        document.getElementById('fname').value = this.cells[1].innerHTML;
        document.getElementById('lname').value = this.cells[2].innerHTML;
        document.getElementById('Country').value = this.cells[3].innerHTML;
        document.getElementById('Mobile').value = this.cells[4].innerHTML;
    };
}

function editRow(){
    table.rows[rIndex].cells[1].innerHTML = document.getElementById("fname").value;
    table.rows[rIndex].cells[2].innerHTML = document.getElementById("lname").value;
    table.rows[rIndex].cells[3].innerHTML = document.getElementById("Country").value;
    table.rows[rIndex].cells[4].innerHTML = document.getElementById("Mobile").value;

}

function editTableDisplay(){
    document.querySelector('.edittable').setAttribute('style','display: block;')
}