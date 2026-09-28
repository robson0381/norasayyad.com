# Especificação de implementação — Redesign v3

## Regra de arquitetura
O HTML principal é gerado. Alterações estruturais devem ser feitas em build.py e regeneradas; estilos globais devem respeitar assets/css/style.css. Não editar manualmente os HTML gerados como solução definitiva.

## Home
### Header
Wordmark Nora Sayyad à esquerda; Work, Current, Commissions, About, Contact; EN / FI. Esconder idioma ainda não implementado.

### Hero
- Desktop: duas zonas. Texto/wordmark à esquerda e retrato real da Nora à direita.
- Usar foto real em alta resolução fornecida pela Nora/Robson, com srcset.
- Aplicar colagem apenas como decoração: papel, recortes suaves, uma borda de tatreez aprovado e ramo de oliveira discreto.
- H1 deve identificar a Nora de forma específica, não apenas "A visual storyteller".
- CTA: Explore work.
- Mobile: retrato é o primeiro impacto; texto sobre área escura ou bloco separado com contraste AA. Não cobrir olhos/rosto.

### Selected projects
Quatro cards em desktop e um por coluna no mobile. Até confirmação de novos trabalhos, usar os projetos reais existentes: From Arrival to Belonging?, Notes of Resistance, Parfyymin tuulahdus e Portraits. Cada card: capa, título, ano/faixa de ano e categoria.

### Credibilidade
Faixa Selected clients & publications com nomes confirmados em PERFIL.md/RELATORIO.md. Não fabricar logos; usar wordmarks em texto até obter arquivos adequados.

### Current / News
Exposição, residência ou publicação em destaque com dados confirmados e CTA View details.

### Fechamento
Imagem real em largura total. Citação somente se for de autoria confirmada da Nora; caso contrário, usar texto editorial sem aspas.

## Work
Grade por projetos, com filtro opcional Documentary / Conceptual / Portraiture. O filtro precisa funcionar por teclado. Mobile empilhado; nada depende de hover.

## Project template
- Intro desktop: texto 34–40%, imagem 60–66%.
- Título em Playfair Display e metadata em Inter.
- Campos: year, category, location, client/partner, exhibitions/publications — somente quando confirmados.
- Corpo com narrativa + imagens em ritmo editorial, sem exigir grade uniforme.
- Navegação anterior / todos / próximo em loop.
- Lightbox opcional acessível: Esc fecha, setas navegam e foco fica preso no modal.
- From Arrival to Belonging? deve usar as fotos reais já catalogadas em content/photos.json; não reproduzir imagens geradas do mockup.

## About
Retrato real da Nora, bio curta primeiro e CV completo depois, dividido por seções. Botão Download CV somente quando houver PDF oficial.

## Current
Lista de exposições/publicações/residências, separando em curso, futuras e passadas. Datas e locais precisam ser confirmados antes de publicar.

## Commissions
Posicionar editorial/documentary, portrait/institutional e trabalhos selecionados. CTA Discuss a project leva ao Contact com assunto pré-selecionado. Não prometer serviços sem apoio nas fontes do repositório.

## Contact
Formulário com tipo de pedido, nome, e-mail, organização e mensagem. E-mail com domínio próprio quando criado; até lá, manter contato confirmado.

## Responsividade
Validar em 1440, 1024, 768 e 390 px. Zero scroll horizontal. Imagens com width/height para evitar layout shift; loading=lazy fora do hero; apenas a imagem principal pode receber prioridade de carregamento.

## SEO
Title e description únicos; URLs curtas; og:image por página. Schema somente quando os dados necessários estiverem corretos.

## Critérios de aceite
- Hero usa fotografia real da Nora.
- Identidade palestina é perceptível por detalhes reais/aprovados, sem dominar todas as páginas.
- Nenhum texto árabe inventado.
- Nenhum fato novo fora das fontes confirmadas.
- Navegação completa em teclado e touch.
- Sem regressão em 390 px e 1440 px.
- build.py continua sendo a fonte da estrutura gerada.
- python3 build.py completa sem erro após a implementação.
