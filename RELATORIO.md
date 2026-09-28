# norasayyad.com — Avaliação e plano de melhorias

Resumo: o currículo da Nora é forte (Washington Post, The Times, Helsinki City Museum, acervos públicos, turnê *The Lost Paintings*), mas o site atual funciona como um arquivo de fotos, não como uma vitrine. As correções abaixo estão ordenadas por impacto ÷ esforço.

Este repositório traz um **protótipo navegável** do site proposto (HTML/CSS estático, sem dependências). Ele serve para validar estrutura, textos e navegação antes de reconstruir no Squarespace ou migrar de plataforma. Os trechos com fundo amarelo são conteúdo que a Nora precisa confirmar ou escrever.

---

## Prioridade 1 — Corrigir já (1 dia, dentro do Squarespace)

| # | Problema | Correção | Onde está no protótipo |
|---|---|---|---|
| 1 | Link "Login Account" e carrinho "0" sem loja | Desativar *Commerce* e *Customer Accounts* em Configurações | Cabeçalho sem login/carrinho |
| 2 | URLs `/work-1` e `/project-one-f5w4d-…` | Renomear os slugs e criar redirecionamentos 301 das URLs antigas | `/work/`, `/work/notes-of-resistance/` |
| 3 | Texto alternativo = nome do arquivo (`4W7A4927.jpg`, `Kopio tiedostosta…`) | Descrever a cena em cada imagem; renomear os arquivos antes do upload | Cada foto tem `aria-label` descritivo |
| 4 | Sem meta description e sem og:image | Preencher *SEO description* por página e definir a imagem social | `<meta name="description">` e `og:image` em todas as páginas |
| 5 | Home sem H1; "A visual storyteller" com 12px, branco, em cima da foto | H1 com o posicionamento, texto ≥ 16px, fora da foto ou sobre uma área escura | H1 + lead na home |
| 6 | Foto de capa em baixa resolução (versão Instagram de 1024×576 esticada) | Enviar o original em ≥ 2400px | Espaço do hero indica o tamanho mínimo |
| 7 | Favicon padrão do Squarespace | Enviar um favicon próprio | `assets/favicon.svg` (monograma NS) |
| 8 | Ícone de menu cortado no celular | Ajustar o padding do cabeçalho mobile | Menu mobile testado a 390px, sem rolagem horizontal |

## Prioridade 2 — Navegação e desempenho (1 semana)

- **Work no celular**: trocar o índice que depende de passar o mouse por uma grade de cards com capa, título, uma linha de descrição e o número de fotos. Isso funciona igual no toque e no mouse.
- **Projetos como histórias**: texto de abertura, ficha (ano, local, imprensa, exposição), legendas e capítulos curtos. Selecionar **15 a 25 fotos** em vez de ~80. O restante pode ir para uma página "arquivo" ou virar outro projeto.
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
6. **Acesso de rede**: o domínio `norasayyad.com` estava bloqueado neste ambiente, então o protótipo usa blocos cinza no lugar das fotos. Liberar o domínio permite puxar as imagens e os textos reais.
