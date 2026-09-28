# Redesign v3 — direção visual escolhida

Status: direção-base escolhida por Robson em 28/09/2026. Este pacote orienta a próxima rodada de implementação visual; fatos biográficos, textos finais, traduções e fotografias novas continuam sujeitos à confirmação da Nora.

## Decisões visuais consolidadas

- Estrutura e hierarquia: usar como base o layout editorial da primeira proposta aprovada na conversa.
- Nome/wordmark: usar a linguagem tipográfica da segunda proposta; referência prática para implementação: Playfair Display ou serif editorial equivalente, com ajuste fino de tracking e quebra em duas linhas quando necessário.
- Hero: usar o tratamento da terceira proposta, mas obrigatoriamente com fotografia real da Nora. Retratos gerados por IA servem apenas como mockup e não entram em produção.
- Identidade palestina: aparecer de forma autoral e sofisticada, principalmente por meio de tatreez aprovado, ramo de oliveira, papel/arquivo, vermelho profundo e verde oliva. Evitar transformar a origem em decoração temática.
- Árabe: nunca usar pseudo-caligrafia ou texto inventado. Qualquer texto árabe precisa vir de conteúdo real e ser revisado por falante competente.
- Fotografias: usar os originais da Nora ou as URLs já catalogadas em content/photos.json. Não baixar e versionar imagens do Instagram.

## Artefatos deste diretório

- DESIGN-SYSTEM.md — cores, tipografia, grid, componentes e linguagem visual.
- IMPLEMENTATION-SPEC.md — comportamento por página, responsividade, acessibilidade e critérios de aceite.
- CONTENT-ASSET-MAP.md — o que já existe no repositório e o que ainda precisa ser fornecido.
- design-tokens.json — tokens para CSS/implementação.
- reference-layout.svg — prancha esquemática 1:1 para orientar o desenvolvimento. Não é peça final e não contém a fotografia real da Nora.

## Princípio de produto

O site deve parecer simultaneamente um portfólio fotográfico contemporâneo, uma publicação editorial e um arquivo vivo. A interface deve desaparecer quando a fotografia entra em cena; referências culturais entram como detalhes recorrentes, não como moldura permanente de todas as imagens.

## Fontes internas obrigatórias

- PERFIL.md
- RELATORIO.md
- content/photos.json
- CLAUDE.md
- CONTRIBUTING.md

Em caso de conflito entre um mockup e fatos/documentos do repositório, os documentos e o conteúdo confirmado prevalecem.
