console.log("Script Carregado - VERSÃO FINAL 🚀");

// Configuração dos botões
var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var produtoId = this.dataset.product
        var action = this.dataset.action
        console.log('Botão clicado:', produtoId, 'Ação:', action)

        if (user === 'AnonymousUser'){
            showToast("⚠️ Faça login para comprar!", "red")
        } else {
            updateUserOrder(produtoId, action)
        }
    })
}

// Envia para o Django
function updateUserOrder(produtoId, action){
    console.log('Enviando dados...')
    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        }, 
        body: JSON.stringify({'produtoId': produtoId, 'action': action})
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log('Sucesso:', data)
        if(action === 'add'){
            showToast("✅ Adicionado ao carrinho!", "green")
        } else if (action === 'remove'){
            showToast("🗑️ Item removido!", "red")
        }
        
       
    })
}

// Cria a Notificação 
function showToast(message, color) {
    var bgClass = color === "red" ? "bg-red-600" : "bg-blue-600";
    var toast = document.createElement("div");
    

    toast.className = `fixed bottom-5 right-5 ${bgClass} text-white px-6 py-4 rounded-xl shadow-2xl flex items-center gap-3 transform transition-all duration-500 translate-y-20 opacity-0 z-50 font-bold border border-white/10`;
    
    toast.innerHTML = `<span class="material-symbols-outlined">shopping_cart</span> <span>${message}</span>`;

    document.body.appendChild(toast);

    setTimeout(() => { toast.classList.remove("translate-y-20", "opacity-0"); }, 100);

    setTimeout(() => {
        toast.classList.add("translate-y-20", "opacity-0");
        setTimeout(() => { toast.remove(); }, 500);
    }, 3000);
}


var btnPagar = document.getElementById('btn-pagar')

if(btnPagar){
    btnPagar.addEventListener('click', function(e){
        submitFormData()
    })
}

function submitFormData(){
    console.log('Iniciando pagamento com Stripe...')

    var url = '/process_order/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        }, 
        body:JSON.stringify({'form': 'pagamento'})
    })
    .then((response) => response.json())
    .then((data) => {
        console.log('Link Stripe:', data);
        
        // Se der erro, o objeto data terá um campo 'error'
        if(data.error){
            showToast("❌ Erro: " + data.error, "red");
        } else {
            // Redireciona para a página da Stripe
            window.location.href = data; 
        }
    })
    .catch((error) => {
        console.error('Erro:', error);
        showToast("❌ Erro ao conectar", "red");
    });
}