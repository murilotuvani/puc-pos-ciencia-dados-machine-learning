# Criar um banco usando Neo4J para Redes Sociais

Roteiro para fazer a tarefa.

Assista novamente a aula ao vivo que o professor ensinou o básico sobre Neo4J e ensinou você a usar a linguagem Cypher de maneira introdutória.

Crie um banco orientado a grafos chamado SocialPUC dentro da sua área Sandbox no Neo4J.

Acrescente nodes que representem professores e estudantes e relacionamentos entre eles. Acrescente arestas interessantes como: Professor A (lecionou para o estudante) B, Professor Y compartilhou material com Estudante C e assim sucessivamente, para todas as necessidades de uma rede social universitária entre professores e alunos.

Faça algumas consultas importantes usando Cypher e justifique porque são importantes (escreva num texto as consultas e o motivo pelos quais são importantes).

Grave um vídeo de até 10 minutos, publique-o como NÃO LISTADO no youtube e acrescente o endereço do vídeo como resposta desta tarefa.

Link para o [Sandbox do Neo4j: https://sandbox.neo4j.com/](https://sandbox.neo4j.com/).


## Conceitos

Aqui vamos discutir a modalagem do banco de dados:
Uma pessoa pode em um determinado momento ser aluno e em outro momento ser professor de uma determinada matéria.
As matérias são partes de um curso, existem cursos de graduação e de pós-graduação.
Um aluno para ser aprovado precisar ter uma frequÊncia acima de X% e ter uma nota média de cima de um outro valor, digamos 70%.
Vamos considerar:
- 75% de frequência para ser aprovado.
- 70% de aproveitamento (nota) para ser aprovado.

Um aluno é matriculado em uma turma de determinada máteria, pois a matéria se repete ano após ano ou semestre após semestre e além disso uma única turma pode alunos de cursos distintos.
As turmas tem aulas e as aulas tem dia e hora e deve haver um registro da presença de cada aluno matriculado em cada turma.

### Exemplificando.

Vamos dizer que existem as seguintes pessoas, cursos e turmas.

### Criando as pessoas

Neste caso vamos utilizar uma biblioteca do Python para criar dados falsos.
Veja a criação destes dados no arquivo dados/criando-pessoas.py

Resultado:
```
{'nome': 'Pedro Miguel Pacheco', 'data_nascimento': datetime.date(1984, 6, 24), 'idade': 40}
{'nome': 'Vitor Gabriel da Luz', 'data_nascimento': datetime.date(2003, 8, 30), 'idade': 21}
{'nome': 'Larissa Pinto', 'data_nascimento': datetime.date(1978, 3, 2), 'idade': 47}
{'nome': 'Fernando Caldeira', 'data_nascimento': datetime.date(1992, 7, 17), 'idade': 32}
{'nome': 'Henry Rezende', 'data_nascimento': datetime.date(1996, 3, 10), 'idade': 29}
{'nome': 'Maria Clara Rodrigues', 'data_nascimento': datetime.date(1992, 2, 21), 'idade': 33}
{'nome': 'Vitor Gabriel Leão', 'data_nascimento': datetime.date(1978, 8, 17), 'idade': 46}
{'nome': 'Ágatha Câmara', 'data_nascimento': datetime.date(1984, 2, 11), 'idade': 41}
{'nome': 'Anthony Gabriel Moura', 'data_nascimento': datetime.date(2004, 9, 5), 'idade': 20}
{'nome': 'Sara Nogueira', 'data_nascimento': datetime.date(1989, 4, 17), 'idade': 36}
```

Limpando o banco de dados

```
MATCH (n) DETACH DELETE n
```

Convertendo para Cipher
```
CREATE (p:PESSOA {nome: 'Pedro Miguel Pacheco', data_nascimento: date({year: 1984, month: 6, day: 24}), idade: 40});
CREATE (v:PESSOA {nome: 'Vitor Gabriel da Luz', data_nascimento: date({year: 2003, month: 8, day: 30}), idade: 21});
CREATE (l:PESSOA {nome: 'Larissa Pinto', data_nascimento: date({year: 1978, month: 3, day: 2}), idade: 47});
CREATE (f:PESSOA {nome: 'Fernando Caldeira', data_nascimento: date({year: 1992, month: 7, day: 17}), idade: 32});
CREATE (h:PESSOA {nome: 'Henry Rezende', data_nascimento: date({year: 1996, month: 3, day: 10}), idade: 29});
CREATE (m:PESSOA {nome: 'Maria Clara Rodrigues', data_nascimento: date({year: 1992, month: 2, day: 21}), idade: 33});
CREATE (i:PESSOA {nome: 'Vitor Gabriel Leão', data_nascimento: date({year: 1978, month: 8, day: 17}), idade: 46});
CREATE (a:PESSOA {nome: 'Ágatha Câmara', data_nascimento: date({year: 1984, month: 2, day: 11}), idade: 41});
CREATE (n:PESSOA {nome: 'Anthony Gabriel Moura', data_nascimento: date({year: 2004, month: 9, day: 5}), idade: 20});
CREATE (s:PESSOA {nome: 'Sara Nogueira', data_nascimento: date({year: 1989, month: 4, day: 17}), idade: 36});
```

Visualizando os dados
```
MATCH (p:PESSOA) RETURN p
```

Criando os cursos de Engenharia de Computação, Análise de Sistemas e Matemática, é de propósito para permitir alunos de curos distintos frequentando a mesma turma.
Também vaos criar o custo de pós-gradução 'Ciência de Dados & Machine Learning'
```
CREATE (cec:CURSO {titulo: 'Engenharia de Computação', tipo: 'Graduação', carga_horaria: 5300});
CREATE (cas:CURSO {titulo: 'Análise de Sistemas', tipo: 'Graduação', carga_horaria: 4100});
CREATE (cm:CURSO {titulo: 'Matemática', tipo: 'Graduação', carga_horaria: 4180});
CREATE (ccd:CURSO {titulo: 'Ciência de Dados & Machine Learning', tipo: 'Pós gradução', carga_horaria: 360});
```

Criando algumas matérias
```
CREATE (mcalc1:MATERIA {titulo: 'Cálculo I', carga_horaria: 110});
CREATE (mcalc2:MATERIA {titulo: 'Cálculo II', carga_horaria: 90});
CREATE (malgo:MATERIA {titulo: 'Algorítmos', carga_horaria: 96});
CREATE (mbdnr:MATERIA {titulo: 'Bancos de Dados não Relacionais', carga_horaria: 92});
CREATE (esta:MATERIA {titulo: 'Estatística', carga_horaria: 80});
CREATE (plpr:MATERIA {titulo: 'Paradigmas de Linguagens de Programação', carga_horaria: 96});
CREATE (inia:MATERIA {titulo: 'Introdução a Inteligência Artificial', carga_horaria: 78});
```

Criando a grade curricular

Primeiro a matéria 'Bancos de Dados não Relacionais' compoem a grade curricular do curso de pós-graduação 'Ciência de Dados & Machine Learning'.
```
MATCH (ccd:CURSO)
WHERE ccd.titulo='Ciência de Dados & Machine Learning'

MATCH (mbdnr:MATERIA)
WHERE mbdnr.titulo='Bancos de Dados não Relacionais'

CREATE (mbdnr)-[ccd_mbdnr:COMPOEM]-> (ccd)
```

Criando a grade curricular dos cursos de graduação.
```
MATCH (cec:CURSO)
WHERE cec.titulo='Engenharia de Computação'
MATCH (cas:CURSO)
WHERE cas.titulo='Análise de Sistemas'
MATCH (cm:CURSO)
WHERE cm.titulo='Matemática'

MATCH (mcalc1:MATERIA)
WHERE mcalc1.titulo='Cálculo I'
MATCH (mcalc2:MATERIA)
WHERE mcalc2.titulo='Cálculo II'
MATCH (malgo:MATERIA)
WHERE malgo.titulo='Algorítmos'

MATCH (esta:MATERIA)
WHERE esta.titulo='Estatística'
MATCH (plpr:MATERIA)
WHERE plpr.titulo='Paradigmas de Linguagens de Programação'
MATCH (inia:MATERIA)
WHERE inia.titulo='Introdução a Inteligência Artificial'

CREATE (mcalc1)-[cm_mcalc1:COMPOEM]-> (cm)
CREATE (mcalc2)-[cm_mcalc2:COMPOEM]-> (cm)
CREATE (esta)-[cm_mesta:COMPOEM]-> (cm)

CREATE (malgo)-[cas_algo:COMPOEM]-> (cas)
CREATE (mcalc1)-[cas_mcalc1:COMPOEM]-> (cas)

CREATE (mcalc1)-[cec_mcalc1:COMPOEM]-> (cec)
CREATE (mcalc2)-[cec_mcalc2:COMPOEM]-> (cec)
CREATE (malgo)-[cec_algo:COMPOEM]-> (cec)

CREATE (esta)-[cec_esta:COMPOEM]-> (cec)
CREATE (inia)-[cec_inia:COMPOEM]-> (cec)
CREATE (plpr)-[cec_plpr:COMPOEM]-> (cec)
```

Vendo a composição dos curos
```
MATCH (m:MATERIA)-[o:COMPOEM]->(c:CURSO)
RETURN c.titulo as Curso, c.tipo as Nível, m.titulo as Matéria
ORDER BY c.titulo, m.titulo
```


Criando as dependências (pré-requisitos) 

Pré-requisitos de Cálculo II

```
MATCH (mcalc1:MATERIA)
WHERE mcalc1.titulo='Cálculo I'
MATCH (mcalc2:MATERIA)
WHERE mcalc2.titulo='Cálculo II'

CREATE (mcalc1)-[:PRE_REQUISITO]-> (mcalc2)
```

Pré-requisitos de Introdução a Inteligência Artificial

```
MATCH (malgo:MATERIA)
WHERE malgo.titulo='Algorítmos'
MATCH (esta:MATERIA)
WHERE esta.titulo='Estatística'
MATCH (plpr:MATERIA)
WHERE plpr.titulo='Paradigmas de Linguagens de Programação'
MATCH (inia:MATERIA)
WHERE inia.titulo='Introdução a Inteligência Artificial'

CREATE (malgo)-[:PRE_REQUISITO]-> (plpr)
CREATE (plpr)-[:PRE_REQUISITO]-> (inia)
CREATE (esta)-[:PRE_REQUISITO]-> (inia)
```

Exibe a matéria de Introdução a Inteligência Artificial a sua árvore de pré requisitos.
```
MATCH (prereq:MATERIA)-[:PRE_REQUISITO*1..]->(inia:MATERIA)
WHERE inia.titulo = 'Introdução a Inteligência Artificial'
RETURN prereq, inia
```

Como ficaram os dados
```
MATCH (n) RETURN n
```

Pode-se fazer a matrícula de alunos em cursos.

Os alunos por ordem de idade:
```
MATCH (p:PESSOA)
RETURN p.nome AS Nome, p.idade AS Idade
ORDER BY p.idade
```

## Selecionando as matrículas por idade
"Vitor Gabriel da Luz"	21 -> Engenharia de Computação
"Henry Rezende"	29 -> Engenharia de Computação
"Fernando Caldeira"	32 -> Engenharia de Computação
"Maria Clara Rodrigues"	33 -> Análise de Sistemas
"Sara Nogueira"	36 -> Matemática
"Pedro Miguel Pacheco" 40 -> Pós

Matriculando os alunos no curos de Engenharia de Computação
```
MATCH (cec:CURSO)
WHERE cec.titulo='Engenharia de Computação'

MATCH (v:PESSOA)
WHERE v.nome='Vitor Gabriel da Luz'

MATCH (h:PESSOA)
WHERE h.nome='Henry Rezende'

MATCH (f:PESSOA)
WHERE f.nome='Fernando Caldeira'

CREATE (v)-[:MATRICULA {ra:23000001}]-> (cec)
CREATE (h)-[:MATRICULA {ra:23000002}]-> (cec)
CREATE (f)-[:MATRICULA {ra:23000003}]-> (cec)
```

Matriculando os outros alunos
"Maria Clara Rodrigues"	33 -> Análise de Sistemas
```
MATCH (cec:CURSO)
WHERE cec.titulo='Análise de Sistemas'

MATCH (v:PESSOA)
WHERE v.nome='Maria Clara Rodrigues'
CREATE (v)-[:MATRICULA {ra:24000001}]-> (cec)
```

"Sara Nogueira"	36 -> Matemática
```
MATCH (cec:CURSO)
WHERE cec.titulo='Matemática'

MATCH (s:PESSOA)
WHERE s.nome='Sara Nogueira'
CREATE (s)-[:MATRICULA {ra:24000002}]-> (cec)
```

"Pedro Miguel Pacheco" 40 -> Pós
```
MATCH (cec:CURSO)
WHERE cec.titulo='Ciência de Dados & Machine Learning'

MATCH (f:PESSOA)
WHERE f.nome='Pedro Miguel Pacheco'
CREATE (f)-[:MATRICULA {ra:25000203}]-> (cec)
```


## Vendo os pré-requisitos.

MATCH p=()-[:PRE_REQUISITO]->() RETURN p LIMIT 25;