<div class="markdown prose w-full break-words dark:prose-invert light"><h1>Cadastro de Veículos</h1><p>Este projeto é um cadastro simples de veículos que utiliza o TinyDB como banco de dados e a biblioteca Pandas para manipulação de arquivos.</p><h2>Funcionalidades</h2><ul><li><p>Cadastrar Veículos: Registra um novo veículo no banco de dados. É necessário informar o número da frota e, caso ainda não esteja cadastrado, a placa do veículo.</p></li><li><p>Procurar Veículos: Pesquisa e exibe informações sobre um veículo cadastrado. É necessário informar o número da frota.</p></li><li><p>Adicionar Despesas: Adiciona uma despesa ao histórico de um veículo cadastrado. É necessário informar o número da frota, o número da nota fiscal, o valor da despesa e uma descrição.</p></li></ul><h2>Como executar o projeto</h2><ol><li>Instale as dependências necessárias através do comando:</li></ol><pre><div class="bg-black mb-4 rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans"><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg" data-darkreader-inline-stroke="" style="--darkreader-inline-stroke:currentColor;"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs">pip install -r requirements.txt
</code></div></div></pre><ol start="2"><li>Execute o arquivo <code>main.py</code>.</li></ol><pre><div class="bg-black mb-4 rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans"><span class="">css</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg" data-darkreader-inline-stroke="" style="--darkreader-inline-stroke:currentColor;"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-css">python <span class="hljs-selector-tag">main</span><span class="hljs-selector-class">.py</span>
</code></div></div></pre><p>O programa exibirá um menu de opções que pode ser selecionado através do número correspondente.</p></div>