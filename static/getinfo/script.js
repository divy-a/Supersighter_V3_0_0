
let id = new URL(window.location.href).searchParams.get("id");

fetch(`/getinfo/${id}`)
    .then(response => response.json())
    .then(response => updatePage(response))
    .catch(error => console.error(error));



function updatePage(data){
    var table = document.getElementById("myTable").getElementsByTagName('tbody')[0];
    table.innerHTML = "";
    for (var key in data) {
      var row = table.insertRow();
      var keyCell = row.insertCell(0);
      var valueCell = row.insertCell(1);
      keyCell.innerHTML = (key.charAt(0).toUpperCase()+key.slice(1)).replace('_', ' ')
      valueCell.innerHTML = data[key];
    }
  }
  