# norasayyad.com — Avaliação e plano de melhorias

Resumo: o currículo da Nora é forte (Washington Post, The Times, Helsinki City Museum, acervos públicos, turnê *The Lost Paintings*), mas o site atual funciona como um arquivo de fotos, não como uma vitrine. As correções abaixo estão ordenadas por impacto ÷ esforço.

Este repositório traz um **protótipo navegável** do site proposto (HTML/CSS estático, sem dependências), montado com o **conteúdo real** do site atual: bio, CV, links de imprensa e as fotos dela, servidas pelo próprio CDN do Squarespace. Ele serve para validar estrutura, textos e navegação antes de reconstruir no Squarespace ou migrar de plataforma. Os trechos com fundo amarelo são conteúdo que a Nora precisa confirmar ou escrever.

## O que o site tem hoje (verificado no código)

| Página | URL atual | Conteúdo |
|---|---|---|
| Home | `/` | Uma foto, "A visual storyteller", botão "View Portfolio" |
| Work | `/work-1` | Índice de 4 projetos, com a foto mudando ao passar o mouse |
| Notes of Resistance | `/work-1/notes-of-resistance` | **86 fotos**, nenhum texto ou legenda |
| Portraits | `/work-1/project-one-f5w4d-z9nem-…` | 19 fotos, nenhum texto |
| From Arrival to Belonging? | `/work-1/project-two-ky966-n329z-…` | 11 fotos (uma repetida) e **o único texto de projeto do site** |
| Parfyymin tuulahdus | `/work-1/parfyymin-tuulahdus` | 3 fotos e só o título; uma das fotos também está em Portraits |
| About | `/about` | Bio forte e CV completo, mas sem foto dela e num bloco único e longo |

Em todas as páginas: link "Login / Account", link para `/cart`, meta description vazia e contato só pelo Gmail.

**Correção à análise anterior:** o arquivo da foto de capa tem 2500×1406 px. A resolução em si é suficiente; o problema é que é uma versão exportada "INSTAGRAM" e mais clara ("valoisampi"). Vale confirmar se existe um original melhor.

**Uma descoberta importante:** o CV é excelente (Helsinki City Museum, Finnish Museum of Photography, HIAP, Kone Foundation, *No Justice, No Peace* premiado, 3 acervos públicos, Women Photograph), mas só aparece no fim da página About. Nada disso chega à home.

---

## Prioridade 1 — Corrigir já (1 dia, dentro do Squarespace)

| # | Problema | Correção | Onde está no protótipo |
|---|---|---|---|
| 1 | Link "Login Account" e carrinho "0" sem loja | Desativar *Commerce* e *Customer Accounts* em Configurações | Cabeçalho sem login/carrinho |
| 2 | URLs `/work-1` e `/project-one-f5w4d-…` | Renomear os slugs e criar redirecionamentos 301 das URLs antigas | `/work/`, `/work/notes-of-resistance/` |
| 3 | Texto alternativo = nome do arquivo (`4W7A4927.jpg`, `Kopio tiedostosta…`) ou vazio | Descrever a cena em cada imagem; renomear os arquivos antes do upload | As 57 fotos do protótipo têm texto alternativo descritivo (`content/photos.json`) |
| 4 | Sem meta description e sem og:image | Preencher *SEO description* por página e definir a imagem social | `<meta name="description">` e `og:image` em todas as páginas |
| 5 | Home sem H1; "A visual storyteller" com 12px, branco, em cima da foto | H1 com o posicionamento, texto ≥ 16px, fora da foto ou sobre uma área escura | H1 + lead na home |
| 6 | Foto de capa é uma exportação "INSTAGRAM" clareada | Enviar o original em ≥ 2500px, sem recompressão | Hero com `srcset` responsivo |
| 7 | Favicon padrão do Squarespace | Enviar um favicon próprio | `assets/favicon.svg` (monograma NS) |
| 8 | Ícone de menu cortado no celular | Ajustar o padding do cabeçalho mobile | Menu mobile testado a 390px, sem rolagem horizontal |

## Prioridade 2 — Navegação e desempenho (1 semana)

- **Work no celular**: trocar o índice que depende de passar o mouse por uma grade de cards com capa, título, uma linha de descrição e o número de fotos. Isso funciona igual no toque e no mouse.
- **Projetos como histórias**: texto de abertura, ficha (ano, local, imprensa, exposição), legendas e capítulos curtos. No protótipo, *Notes of Resistance* passou de 86 para **25 fotos**, em dois capítulos: *Black Lives Matter, Finland 2020* e *Palestine solidarity, Helsinki*. É uma seleção provisória, para a Nora revisar. As fotos repetidas entre projetos foram removidas.
- **Peso da página**: com ~80 fotos, a página de *Notes of Resistance* ficou quase um minuto em branco no teste mobile. Com a seleção enxuta, o *lazy-loading* e imagens em WebP/AVIF, a meta é chegar a menos de 2,5 s de LCP no 4G.
- **Navegação entre projetos**: anterior/próximo **em loop** + "Todos os projetos" no fim de cada página. Visualizador de fotos com setas, deslizar para os lados e Esc.
- **Contato**: página própria com formulário (tipo de pedido: comissão, exposição, imprensa, palestra, prints), prazo de resposta e e-mail com domínio próprio (`contact@norasayyad.com`). O Gmail sai do rodapé.

## Prioridade 3 — Destacar e reter (2 a 4 semanas)

- **Home como vitrine**: posicionamento claro, faixa "Publicado & exposto em", 3 projetos em destaque, bloco "Em turnê agora" (*The Lost Paintings*) e um trecho da bio.
- **Página de Comissões**: retratos, editorial/documental, palestras e oficinas, cada um com um botão que já abre o formulário com o assunto certo.
- **News/Exposições**: a turnê em andamento dá um motivo para voltar ao site. Atualizar a cada abertura, publicação ou palestra.
- **About**: retrato profissional, bio curta em 3ª pessoa (pronta para imprensa), CV em seções recolhíveis e PDF para baixar.
- **Canais de retorno**: newsletter (Squarespace Email Campaigns ou Mailchimp), LinkedIn e Instagram no rodapé.
- **Idiomas**: seletor EN / FI / SV; começar pelo finlandês na Home, Comissões e Contato.
- **Prints (opcional)**: se ela quiser vender, o carrinho volta *de propósito*, com uma página "Prints" de tiragem limitada.

## Instagram (@norasayyad)

- Usar o mesmo nome em todos os canais ("Nora Sayyad" ou "Elli Nora Sayyad").
- Trocar a selfie no espelho por um retrato profissional ou uma foto autoral forte.
- Renomear os destaques: Exposições · Projetos · Imprensa · Comissões · Palestras. Arquivar os de viagem pessoal.
- Chamada para contratar na bio: "📩 Comissões: contact@norasayyad.com" + link para `/services/`.
- O feed não foi avaliado, porque o Instagram exige login para mostrar os posts.

## Como medir o resultado

Antes e depois (Squarespace Analytics + Google Search Console): taxa de rejeição da home, cliques de Home → projeto, tempo nas páginas de projeto, envios do formulário de contato, inscritos na newsletter e impressões de busca para "Nora Sayyad photographer".

## O que ainda falta para uma avaliação definitiva

1. **Objetivo principal**: comissões, circuito de arte/curadoria ou venda de prints. Isso define a ordem do menu e o CTA principal.
2. **Público-alvo**: editores, ONGs, instituições ou clientes particulares.
3. **Dados**: acesso de leitura ao Squarespace Analytics e ao Search Console.
4. **Conteúdo real**: bio, CV completo, legendas, links de imprensa e as fotos originais em alta resolução.
5. **Referências**: 2 ou 3 sites de fotógrafos de que ela gosta.
6. **Fotos que faltam**: um retrato profissional da Nora (para a About e a home) e vistas das exposições, principalmente de *The Lost Paintings*. No protótipo, esses espaços aparecem como blocos cinza.
7. **Datas da turnê** *The Lost Paintings* em cada local.

## Decisões

Registro das decisões do projeto: data, decisão e quem decidiu. Novas entradas vão no topo.

| Data | Decisão | Quem |
|---|---|---|
| 28/09/2026 | Direção Editorial / Archive in Motion adicionada ao protótipo como nova opção visual, sem substituir as demais | Robson |
| 28/09/2026 | Opções da versão 2 (Reportagem, Cartas, Tatreez, Sequências) publicadas num link privado para apresentar à Nora; Tatreez marcada como favorita | Robson |
| 28/09/2026 | Versões 1 e 2 guardadas como opções adicionais; conceitos novos (Símbolos, Rota, Visível, Dois lares) em `opcoes/` | Robson |
| 28/09/2026 | Fotos baixadas do Instagram não entram no repositório; usar originais da Nora | Robson |
