# Especificação do redesign — Nora Sayyad

Status: **direção principal definida / protótipo em validação**  
Direção principal: **Editorial / Archive in Motion**  
Alternativa de apresentação: **Archive / Memory**

Esta especificação descreve o comportamento esperado do site independentemente de a implementação final permanecer estática ou migrar para Astro + CMS.

## 1. Objetivo

Criar uma presença digital que funcione simultaneamente como:

1. portfólio artístico;
2. portfólio documental/editorial;
3. apresentação para curadores e instituições;
4. ponto de entrada para comissões;
5. arquivo vivo de exposições, imprensa e projetos.

A interface deve servir à fotografia, não competir com ela.

## 2. Identidade principal

### Conceito

**Editorial / Archive in Motion**

Referências funcionais: livro de fotografia contemporâneo, revista cultural, catálogo de exposição e arquivo vivo.

A linguagem não deve parecer um template genérico de fotógrafo.

### Tokens de cor

| Token | Valor | Uso |
|---|---|---|
| Paper | `#F3F0E8` | fundo principal |
| Surface | `#FBFAF6` | campos e superfícies auxiliares |
| Ink | `#111111` | texto e contraste principal |
| Deep Cobalt | `#17345F` | CTA institucional, blocos especiais e acento |
| Olive | `#727454` | acento secundário |
| Oxide Red | `#A54A3F` | acento raro / editorial |
| Editorial Gray | `#AAA69D` | informação secundária |

Regra: aproximadamente 80% da experiência deve permanecer em Paper / Ink / fotografia. A cor é apoio, não protagonista.

### Tipografia

- Display/editorial: **Newsreader**
- Interface/metadados: **Manrope**
- Fallbacks devem permanecer definidos no CSS.
- Evitar logotipo gráfico complexo: a wordmark “NORA SAYYAD” é a marca principal.

### Escala

- H1: `clamp(3rem, 7vw, 6.4rem)`
- Hero display: até ~8.5rem em desktop
- H2: `clamp(2.2rem, 4.5vw, 4.7rem)`
- Metadados: 0.63–0.70rem, uppercase, tracking ampliado
- Corpo: 16px desktop; 14px em telas estreitas

## 3. Grid e responsividade

- largura máxima de conteúdo: **1420px**
- gutter fluido: `clamp(16px, 3vw, 38px)`
- breakpoint tablet/menu: **960px**
- breakpoint mobile compacto: **620px**

### Regras

Desktop:
- composições assimétricas são permitidas;
- imagens podem ter proporções diferentes;
- evitar grades excessivamente uniformes.

Tablet:
- grids de quatro colunas passam para duas;
- seções de três colunas passam para uma.

Mobile:
- projeto vira fluxo vertical;
- nenhum conteúdo pode depender de hover;
- menu ocupa viewport;
- títulos devem manter presença editorial sem causar overflow.

## 4. Navegação

Menu principal:

`Work · Current · Commissions · About · Contact · EN / FI`

### Requisitos

- header sticky;
- estado ativo visível;
- menu mobile acessível por botão;
- `aria-expanded` sincronizado;
- Escape fecha o menu;
- clique num link fecha o menu;
- navegação por teclado completa.

FI é apresentado como idioma planejado enquanto não houver versão revisada.

## 5. Home

Ordem oficial:

1. Hero
2. Selected projects
3. Selected clients & publications
4. Current / selected press
5. Manifesto visual
6. About
7. Commissions
8. Footer

Newsletter is intentionally deferred in the presentation prototype until a provider/backend is chosen.

### Hero

- 4 imagens de amostra;
- troca **manual**, sem autoplay obrigatório;
- índice real `01 / 04`;
- setas anterior/próximo;
- H1 “NORA SAYYAD”;
- posicionamento curto;
- CTA para Work.

Quando Nora escolher a foto principal e a sequência final, as amostras são substituídas.

## 6. Work

A ordem atual do site é preservada como baseline:

1. Portraits
2. From Arrival to Belonging?
3. Parfyymin tuulahdus
4. Notes of Resistance

A Home pode usar outra ordem editorial de destaques sem alterar o índice completo.

Cada card deve mostrar:

- capa;
- título;
- teaser;
- quantidade ou metadado;
- funcionamento idêntico em mouse e toque.

## 7. Página de projeto

Estrutura:

1. breadcrumb;
2. título;
3. teaser;
4. statement;
5. ficha técnica;
6. narrativa fotográfica;
7. capítulos opcionais;
8. legendas;
9. lightbox;
10. Previous / All projects / Next.

### Imagens

- preservar proporção original sempre que possível;
- não transformar toda fotografia em crop 4:5;
- landscape pode ocupar largura maior;
- portrait pode aparecer em largura reduzida e alternar alinhamento;
- lazy loading após os primeiros elementos;
- lightbox com teclado, swipe e Escape.

### Notes of Resistance

O site atual possui **86 imagens**.

Regra:
- as 86 ficam preservadas no inventário;
- a página pública usa uma seleção curada por padrão;
- uma galeria completa pode existir separadamente se Nora quiser;
- não voltar ao comportamento de carregar dezenas de imagens imediatamente.

Existe uma página interna de revisão em:

`/review/notes-of-resistance/`

Ela é `noindex,nofollow`.

## 8. About

Estrutura:

1. retrato da Nora;
2. bio curta;
3. bio expandida;
4. Selected exhibitions;
5. Awards & residencies;
6. Public collections;
7. Selected assignments / press;
8. Talks / teaching / juries;
9. Education;
10. Memberships;
11. download do CV;
12. Contact.

O currículo completo continua acessível, mas a primeira tela deve comunicar a carreira sem exigir leitura integral.

## 9. Current

Conteúdo elegível:

- exposições em cartaz ou futuras;
- residências;
- palestras;
- matérias/editoriais recentes;
- novos projetos.

Título e status devem vir de conteúdo confirmado. Um item que ainda é “working title” continua identificado dessa forma.

## 10. Commissions

Categorias iniciais:

- Portraits
- Editorial & documentary
- Talks
- Workshops

Cada categoria leva ao Contact com assunto pré-selecionável.

Não usar linguagem de venda agressiva como “Hire me”.

## 11. Contact

Campos:

- nome;
- e-mail;
- organização;
- assunto;
- mensagem.

Assuntos:

- Commission
- Exhibition / curatorial
- Press
- Talk or workshop
- Prints
- Other

No protótipo, o formulário abre um rascunho estruturado no aplicativo de e-mail do visitante. Produção exige backend real antes de publicar.

## 12. Fotografias e pipeline

### Estado atual

- `content/photos.json`: 58 referências estruturadas com dimensões e alt text.
- `content/current-site-inventory.json`: inventário completo do site atual e as 86 URLs de Notes of Resistance.
- `content/sample-assets.json`: proveniência e status de substituição dos assets provisórios usados no protótipo.
- `REFERENCE_BUNDLE.md`: resumo das 346 imagens fornecidas como referência de curadoria; essas cópias não são masters de produção.
- imagens de amostra: CDN atual do Squarespace.

### Estados futuros do asset

Cada fotografia de produção deve ter:

```text
id
project
source/original filename
width
height
alt
caption
date
location
credit
rights/approval status
publication status
hero eligibility
```

### Regras

- não usar download de Instagram como master;
- não guardar masters fotográficos pesados no Git;
- original deve substituir sample antes da entrega final quando disponível;
- gerar formatos e tamanhos responsivos;
- preservar crédito e direitos.

## 13. SEO e migração

Cada página precisa de:

- title próprio;
- meta description;
- canonical;
- Open Graph;
- social image;
- heading hierarchy correta;
- alt text;
- URL legível.

Rotas antigas ficam mapeadas em:

`content/redirects.json`

Mapa editorial completo:

`MIGRATION_MAP.md`

Na migração de domínio, redirects devem ser **301**.

## 14. Acessibilidade

Mínimo obrigatório:

- skip link;
- contraste AA;
- foco visível;
- navegação sem mouse;
- menu com ARIA;
- alt text descritivo;
- lightbox com fechamento por Escape;
- botões com labels;
- headings em ordem lógica;
- nenhuma interação crítica hover-only;
- respeitar `prefers-reduced-motion` na fase de acabamento.

## 15. Performance

Metas de projeto:

- não carregar o arquivo completo de 86 fotos na página principal do projeto;
- `srcset` e `sizes`;
- lazy loading;
- Hero priorizado;
- evitar framework JS desnecessário para conteúdo estático;
- animações limitadas a opacity / transform;
- preservar dimensões para reduzir layout shift.

## 16. Arquitetura técnica

### Protótipo atual

```text
GitHub
  ↓
Python build scripts
  ↓
HTML + CSS + JavaScript vanilla
  ↓
Squarespace CDN (samples)
```

Vantagens: simples, rápido e fácil de auditar durante definição de design.

### Produção proposta

```text
GitHub
  ↓
Astro + TypeScript
  ↓
Sanity CMS
  ↓
Vercel
  ↓
norasayyad.com
```

A migração para Astro/CMS só deve acontecer quando a estrutura e o conteúdo estiverem suficientemente aprovados. Evitar reescrever o protótipo cedo demais.

## 17. CMS — modelos previstos

### Project
- title
- slug
- category
- year
- teaser
- statement
- facts[]
- cover
- gallery[]
- chapters[]
- press[]
- exhibitions[]
- published

### Photo
- asset
- alt
- caption
- credit
- date
- location
- rights
- originalReceived

### Current item
- type
- title
- startDate
- endDate
- venue
- location
- description
- image
- externalLink
- status

### Press
- outlet
- title
- date
- link
- role

## 18. Alternativa visual

**Archive / Memory** fica em `/opcoes/memoria/`.

Ela serve para mostrar uma segunda interpretação da identidade de Nora:

- cartas;
- arquivo familiar;
- proveniência;
- notas marginais;
- deslocamento;
- memória;
- tatreez usado de forma discreta.

Ela **não substitui a direção principal** sem decisão explícita.

## 19. Critério de “pronto para apresentar”

Pode ser mostrado à Nora quando:

- Home principal estiver funcional em desktop/mobile;
- Work e projetos estiverem navegáveis;
- About estiver coerente com o site atual;
- todas as amostras estiverem claramente marcadas como provisórias;
- Archive / Memory estiver acessível como alternativa;
- mapa de migração e pendências estiverem documentados.

## 20. Critério de “pronto para substituir o site”

Além do anterior:

- originais aprovados;
- statements e captions aprovados;
- formulário real;
- CMS ou rotina de atualização definida;
- EN revisado e política para FI definida;
- redirects testados;
- analytics configurado;
- domínio/DNS com plano de rollback;
- validação mobile e acessibilidade;
- performance auditada.

## 21. QA automatizado

O repositório inclui duas camadas de validação:

- `qa.py`: links internos, H1, alt text, IDs duplicados, formulários mortos, inventário e artefatos obrigatórios;
- `visual-qa.mjs`: screenshots Playwright em 1440×1000 e 390×844, além de verificação de overflow horizontal, H1 e alt text.

GitHub Actions recompila os geradores antes da validação para detectar regressões de sintaxe e estrutura.
