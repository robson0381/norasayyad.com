# Design system — Redesign v3

## Direção
Editorial contemporâneo, silencioso e tátil. A fotografia continua dominante. O design combina papel claro, serif forte, interface sans discreta e pequenos sinais de memória e arquivo.

## Paleta
- paper: #F0F2EA — fundo principal.
- canvas: #2E2E2E — texto e fundos escuros pontuais.
- olive: #4A5A3C — microdetalhes e ramo de oliveira.
- deep-blue: #204B6F — metadata e links.
- heritage-red: #882E2E — CTAs e detalhes de bordado.
- stone: #C9B8A1 — bordas e painéis suaves.
- white: #FFFFFF — contraste sobre foto escura.

Paper + canvas devem dominar. As outras cores entram como acentos.

## Tipografia
- Display/wordmark: Playfair Display 600–700.
- Interface/corpo: Inter 400–600.
- Wordmark: caixa alta; pode quebrar NORA / SAYYAD em duas linhas.
- Corpo desktop: 16–18 px, line-height 1.55–1.7.
- Corpo mobile: mínimo 16 px.
- Metadata: 11–13 px, caixa alta, tracking 0.08–0.14 em.

## Grid
- Max-width: 1440 px.
- Gutter: 32 px desktop, 24 px tablet, 18 px mobile.
- Hero desktop: cerca de 46/54 ou 48/52; texto nunca cobre o rosto.
- Cards: 4 colunas desktop, 2 tablet, 1 mobile.
- Ritmo vertical: 16, 24, 32, 48, 72, 96 e 128 px.

## Componentes
### Header
Wordmark à esquerda; Work, Current, Commissions, About, Contact; EN / FI. Mobile com menu simples.

### Hero
Retrato real da Nora obrigatório. Usar fotografia + papel/arquivo sutil + uma faixa de padrão aprovado perto da extremidade, nunca sobre o rosto. Ramo de oliveira opcional e discreto. CTA principal: Explore work. Sem slideshow automático.

### Cards
Imagem dominante, título serif e metadata curta. Hover máximo de 1.02. Nada essencial pode depender de hover.

### Referências culturais
- Tatreez: somente padrão verificado/aprovado pela Nora.
- Usar em poucos pontos: hero, separador, rodapé ou metadata relacionada.
- Ramo de oliveira: ilustração linear, monocromática e discreta.
- Qualquer texto árabe deve ser real e revisado; nunca usar pseudo-caligrafia.

## Movimento
160–220 ms para hover/focus; 220–320 ms para drawer/menu; respeitar prefers-reduced-motion. Sem parallax agressivo ou scroll hijacking.

## Acessibilidade
WCAG AA, focus visível, alt text descritivo, navegação por teclado e nenhum texto essencial embutido em imagem.

## Não fazer
- Retrato de IA da Nora em produção.
- Pseudo-árabe.
- Textura pesada sobre fotografias.
- Citações, títulos, datas ou clientes inventados.
- Padrões culturais genéricos tratados como autênticos.
