- Pra rodar basta executar o main.py

- Tem uma função no postgre.py que conecta ao banco de dados, então é so importar e usar como: 
conn = conectar_banco_dados()
cursor = conn.cursor()

e tá feito!

- Outra coisa sobre essa função, veja ela primeiro antes de baixar o postgre para usar essas mesmas informações,
ou após criar sua conta e tudo mais, você entra no postgre.py e coloca suas informações como você criou, se
precisar de ajuda ou tiver alguma dúvida é só falar!

- Quando rodar a primeira vez as tabelas serão criadas, então não se preocupe com isso, mas você deve criar
o database manualmente ou com comandos do unix.

- Pra quem for fazer a GUI e a db dos perfis, use a pasta users, o código já ta bagunçado então imagina sem
essa organização básica :/

- Dica: você pode usar como refência o código que eu usei pra fazer as operações dos sistemas, mas vai ter
que fazer algumas alterações e adições, ate porque, os sistemas so tem o codigo e o nome, os usuários/perfis
precisam de mais itens de acordo com o trabalho.

- Não está sendo usado tkinter e sim customtkinter, ele tem tudo que o tkinter tem, com a diferença de que ele é
mais fácil de usar e a documentação dele é mais simples e ele ja tem alguma customização pré-feita, levem
em conta que não estamos com o grupo total nesse trabalho então temos que focar no essencial, caso haja tempo
e interesse dos envolvidos, é possivel mudar a customização depois, link: https://customtkinter.tomschimansky.com

- Penso em remover a parte de Login, tem que ver se está pedindo isso no trabalho.

- Caso precisar de ajuda so me chamar no zap, talvez eu possa ajudar.

- AVISO: Em questão do "fetching" de usúarios, quem não souber o que é pode me perguntar depois, quando ele for
apresentado na janela, ele DEVE ser acessivel, clicando nele deve abrir outra janela com todas as informações
do mesmo, isso será necessário porque uma das condições do trabalho é que cada usuário tenha uma descrição no
banco de dados e não vai ser possivel ver essa informação fazendo como eu fiz com sistemas, será necessário
abrir outra janela ou fazer um Dropdown, acredito que a janela seja mais simples. 

- A matriz é a ultima parte, pois precisa do produto e todos os cadastros, tanto de sistemas quanto de perfis para
montar o grafico da matriz.#   m a t r i z _ S o D 
 
 
