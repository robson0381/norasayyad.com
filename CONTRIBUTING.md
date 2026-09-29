# Como colaborar neste repositório

Guia para quem trabalha no novo site da Nora Sayyad: você, a Nora, outros colaboradores e as sessões do Claude. Leia antes da primeira alteração.

## 1. Para que serve o repositório

É o **protótipo** do novo norasayyad.com. Ele não é o site no ar: o site atual continua no Squarespace. Aqui se testam estrutura, textos e visual antes de reconstruir no Squarespace ou migrar de plataforma.

| Arquivo ou pasta | O que é | Pode editar à mão? |
|---|---|---|
| `build.py` | Gera o site completo (home, projetos, About, Commissions, News, Contact) | Sim: **fonte da verdade** do protótipo |
| `build_options.py` | Gera os 6 conceitos atuais em `opcoes/` (Editorial, Arquivo/Memória, Símbolos, Rota, Visível, Dois lares) | Sim |
| `build_editorial.py` | Fonte do conceito Editorial / Archive in Motion usado por `build_options.py` | Sim |
| `build_memory.py` | Fonte da alternativa visual Archive / Memory | Sim |
| `build_options_v2.py` | Gera a versão 2 em `opcoes/v2/` (Reportagem, Cartas, Tatreez, Sequências) | Sim |
| `content/photos.json` | Lista de fotos com texto alternativo, largura e altura | Sim |
| `assets/` | CSS, JS e favicon do protótipo principal | Sim |
| `index.html`, `work/`, `about/`, `services/`, `news/`, `contact/` | **Gerados** por `build.py` | **Não**: edite o gerador e rode de novo |
| `opcoes/*/index.html` | **Gerados** pelos `build_options*.py` | **Não** |
| `opcoes/v1/` | Primeira rodada de opções, congelada (sem gerador) | Só para correções pequenas |
| `RELATORIO.md`, `PERFIL.md` | Avaliação do site atual e perfil público da Nora | Sim |

## 2. Rodar localmente

Precisa de Git e Python 3. Não há dependências.

```sh
git clone https://github.com/robson0381/norasayyad.com.git
cd norasayyad.com
python3 build.py && python3 build_options.py && python3 build_options_v2.py
python3 -m http.server 8000
```

Abra http://localhost:8000 (protótipo) e http://localhost:8000/opcoes/ (conceitos).

## 3. Fluxo de trabalho

1. **`main` é a versão aprovada.** Ninguém envia direto para `main`.
2. Para cada mudança, crie um branch a partir de `main`, com nome curto e descritivo:
   - `conteudo/letters-to-mothers`, `visual/tatreez-mobile`, `correcao/menu-celular`
   - sessões do Claude usam `claude/...`
3. Abra um **pull request** para `main` e preencha o modelo (ele aparece sozinho).
4. **Quem revisa:**
   - mudanças de texto sobre a Nora, fotos ou escolha de visual: **a Nora aprova**;
   - mudanças técnicas (código, layout, correções): outra pessoa do projeto revisa.
5. Depois de aprovado, faça *merge* e apague o branch.

Um PR deve tratar de **um assunto só**. Uma foto nova e uma mudança de layout vão em PRs separados.

## 4. Mensagens de commit

- Em inglês ou português, no imperativo e com até ~70 caracteres na primeira linha:
  `Add Jordan diaries project page`, `Corrige menu cortado no celular`.
- Se precisar explicar, deixe uma linha em branco e escreva o porquê no corpo.
- Não misture arquivos gerados de um assunto com código de outro.

## 5. Regras de conteúdo (as mais importantes)

### Fotos
- **Só a Nora decide quais fotos entram.** Toda foto nova precisa da aprovação dela no PR.
- **Pessoas retratadas:** fotos com pessoas identificáveis (retratos, crianças, *Letters to Mothers*, *From Arrival to Belonging*) só vão para o site no ar com a confirmação dela de que o uso foi autorizado.
- **Originais, não cópias do Instagram.** Imagens baixadas do Instagram são recomprimidas e servem só como provisórias. **Não as envie ao repositório.** Use um espaço reservado (`ph(...)` nos geradores ou `.ph` no CSS) até chegar o original.
- Envie os originais com pelo menos **2500 px** no lado maior. As fotos atuais vêm do CDN do Squarespace pelo `content/photos.json`.
- **Texto alternativo obrigatório:** descreva a cena (quem, o quê, onde), nunca o nome do arquivo. Exemplo: "A woman holds up a hand-lettered Black Lives Matter sign".

### Textos
- Fatos sobre a Nora (datas, exposições, prêmios, publicações) precisam de uma fonte: o CV, o site atual, uma legenda dela ou uma matéria. Anote a fonte no PR.
- Conteúdo ainda não confirmado fica marcado com `<span class=todo>…</span>`, que aparece em amarelo. **Nada com `todo` vai para o site no ar.**
- Citações de outras pessoas (o pai de Mariam, Marika, Noor Assad) só com a fonte e, no site no ar, com a autorização delas.
- Árabe, finlandês e sueco: peça revisão a um falante nativo (de preferência a própria Nora) antes de publicar.
- Idioma do site: inglês primeiro; finlandês e sueco estão planejados.

### Nome e contato
- Use o mesmo nome em todo lugar ("Nora Sayyad", até ela decidir outra forma).
- O e-mail vem da constante `EMAIL` em `build.py`. Troque só lá quando existir o endereço com domínio próprio.

## 6. Checklist antes de abrir o PR

- [ ] Rodei os geradores e enviei os arquivos gerados junto
- [ ] Vi as páginas no computador **e** com 390 px de largura (modo celular do navegador)
- [ ] Nenhuma página rola para o lado no celular
- [ ] Toda imagem nova tem texto alternativo descritivo
- [ ] Nenhum link quebrado (`/work/...`, `/about/`, etc.)
- [ ] Nenhuma foto baixada do Instagram foi adicionada ao repositório
- [ ] Textos novos sobre a Nora têm fonte indicada no PR

## 7. Decisões e discussões

- Registre decisões importantes (visual escolhido, estrutura, plataforma) em `RELATORIO.md`, na seção de decisões, com data e quem decidiu.
- Dúvidas e propostas vão numa *issue* do GitHub, não em mensagens soltas, para ficarem registradas.
- A opinião da Nora sobre o próprio trabalho sempre prevalece.

## 8. Sessões do Claude

As sessões do Claude seguem este guia e o `CLAUDE.md`. Elas trabalham em branches `claude/...`, abrem PR como rascunho e não fazem *merge* sozinhas.
