

function login(){
    let btn_value = document.getElementById('btn').value
    document.getElementById('btn').value = ''
    document.getElementById('spin').style.visibility = 'visible'
    

    fetch(`/admin/update?code=${document.getElementById('code').value}&durl=${document.getElementById('durl').value}&key=${document.getElementById('key').value}`)
    .then(response =>{ if(response.status == 200){
        alert('Updated')
    }
    else{
        alert('Failed to Update')
    }

    document.getElementById('spin').style.visibility = 'hidden',
    document.getElementById('btn').value = btn_value

    
})
    .catch(error => alert(error));
}