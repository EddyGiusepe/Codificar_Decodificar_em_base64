# Algoritmo de Codificação Base64 


![image](https://user-images.githubusercontent.com/69597971/151281080-991efd66-fe18-4841-9c33-5d3a5cca78bf.png)
 
**Base64** é um algoritmo de codificação (``encoding``) que permite transformar qualquer caractere de qualquer idioma em um alfabeto que consiste em letras latinas, dígitos e sinais. Com isso podemos converter caracteres especiais como os logogramas (_símbolo ou grafema único que denota um conceito concreto ou abstrato da realidade_) chineses, emoji e até imagens em uma sequência “legível” (para qualquer computador), que pode ser salvo e/ou transferido para qualquer outro lugar. É utilizado frequentemente para transmitir **dados binários** por meio de transmissões que lidam apenas com texto, como, por exemplo, para enviar imagens e arquivos em anexo por e-mail.

Seu alfabeto é constituído por **64 caracteres ([A-Z],[a-z],[0-9], “/” e “+”)** - Ver Tabela abaixo, o que deu  origem ao seu nome. O carácter ``=`` é utilizado como um sufixo especial e a especificação original (RFC 989) definiu que o símbolo ``*`` pode ser utilizado para delimitar dados convertidos, mas não criptografados, dentro de um *stream*.

![image](https://user-images.githubusercontent.com/69597971/151285248-90445f72-fae5-4505-91b9-9b261938ab76.png)


## O Base64 é seguro? posso usar como método de criptografia?

O algoritmo de codificação do **Base64 não é um algoritmo de criptografia**, ele é facilmente decodificado, portanto não deve ser utilizado como método de criptografia segura. Não utilize essa técnica para proteger dados sensíveis, para isso recorra a [métodos de criptografia seguros](https://cryptoid.com.br/valid/tipos-de-criptografia-conheca-os-10-mais-usados-e-como-funciona-cada-um/).


**Nota:** 
para saber como funciona este algoritmo de codificação, [click aqui](https://marquesfernandes.com/self/o-que-e-base64-para-que-serve-e-como-funciona/).





Links de pesquisa:

* [O que é Base64, para que serve e como funciona?](https://marquesfernandes.com/self/o-que-e-base64-para-que-serve-e-como-funciona/)
* [Algoritmo de Codificação Base64](https://medium.com/swlh/base64-encoding-algorithm-42abb929087d)
* [Vídeo do YouTube: codificação base64](https://www.youtube.com/watch?v=L-cXtP24vAw)
* [Vídeo do YouTube: o que é base64? para que serve a base64](https://www.youtube.com/watch?v=JFXrBkdCAeQ)


Exemplo, básico, em Python:

* [base64 em Python](https://www.youtube.com/watch?v=HY5sEph1cg8)




Thanks God!








