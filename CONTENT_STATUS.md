# Conteúdo pendente para produção

Status em 29/09/2026. O protótipo principal já não depende de textos `todo` visíveis. As pendências mais claras agora são **ativos originais e aprovação editorial**, não layout.

## Imagens que ainda precisam de original/aprovação

| Uso | Estado atual | O que pedir à Nora |
|---|---|---|
| Home — bloco About | placeholder | 1 retrato profissional/autoral da Nora em alta resolução |
| About — retrato principal | placeholder | pode ser o mesmo retrato da Home ou uma segunda opção |
| Current — The Lost Paintings | placeholder | instalação/exhibition view autorizado |
| Current — Förkolnade Minnen / Muistoihin Hiiltyneet | placeholder | vista da exposição ou obra autorizada |

## Fotografias já utilizáveis como amostra

O protótipo usa o CDN público do Squarespace para demonstrar a estrutura:

- Portraits
- From Arrival to Belonging?
- Parfyymin tuulahdus
- Notes of Resistance
- Home / Current / manifesto visual

Essas referências são **amostras de migração**. Antes de produção, o ideal é substituir as imagens escolhidas pelos originais fornecidos/aprovados por Nora.

## Notes of Resistance

- 86 imagens do site atual estão catalogadas no inventário.
- 25 estão estruturadas no protótipo público atual.
- a página interna `/review/notes-of-resistance/` existe para fazer a seleção junto com Nora.
- a decisão final deve ser editorial: quais fotos ficam na sequência principal e se haverá um arquivo completo separado.

## Texto que merece confirmação de Nora

Mesmo quando baseado no site/CV atual, estes itens devem ser confirmados antes da publicação definitiva:

- posicionamento curto da Home;
- bio curta e bio expandida;
- ordem e seleção de projetos destacados;
- wording de Commissions;
- títulos provisórios/ongoing work;
- legendas, datas e locais de cada fotografia;
- datas/status de exposições futuras ou recém-encerradas;
- prazo de resposta no contato, se quisermos exibi-lo;
- versão em finlandês.

## Entrega de originais

Para cada imagem final, registrar:

```text
arquivo original
projeto
largura / altura
alt text
legenda
data
local
crédito
direitos / autorização
pode ser hero? sim/não
```

Evitar masters vindos de Instagram. O pacote de referência fornecido continua documentado em `REFERENCE_BUNDLE.md`.

## Versão em finlandês (/fi/)

- Todas as páginas principais têm versão finlandesa em `/fi/`, gerada por `build.py` a partir de `content/fi.json` (texto em inglês → finlandês).
- **A tradução é um rascunho e precisa de revisão por falante nativo** (de preferência a Nora) antes de publicar. Para corrigir, edite só o valor em finlandês em `content/fi.json` e rode `python3 build.py`.
- Nomes de projetos, títulos de obras e instituições ficam no original.
- `content/fi-missing.txt` lista qualquer texto novo do site que ainda não tem tradução (hoje: nenhum). Texto sem tradução aparece em inglês na versão FI.

## Visible Palestine (antes "Untitled: Palestine")

- Página própria em `/news/visible-palestine/`, com capa no cartão da Current e 8 fotos da residência UA Miniresidency e do pop-up na HIAP (18/12/2025). Fotos fornecidas por Robson em 30/09/2026, com autorização de uso no protótipo.
- O texto da página resume a apresentação pública da HIAP/UrbanApa sobre a exposição.
- **Pessoas identificáveis** (outras residentes e visitantes): confirmar com a Nora a autorização de cada uma antes do site no ar.
- As fotos têm cerca de 800 px de largura; para a versão final, pedir os originais em alta resolução.

## Career history: avisar a Nora

- **No Justice, No Peace / Vuoden Huiput:** o CV do site dela lista o ouro (categoria Jokerit) em **2021**, mas a página da competição (https://vuodenhuiput.fi/work/no-justice-no-peace/) registra **"2020 Kultahuippu, Jokeri"**. O protótipo usa **2020**, conforme a fonte, com link para a página. Confirmar com ela e, se for o caso, corrigir também o site atual.
- O prêmio **Kauneimmat kirjat** (Most Beautiful Books, Special Books) continua em 2021, como no CV dela. Antes os dois prêmios apareciam juntos numa linha só; agora são duas entradas, como no site oficial.
- Entradas do protótipo que **não estão** no CV do site dela, vindas das legendas públicas do Instagram: prêmio ETMU 2023 (Palestinian Voices in Finland) e Helsinki Cultural Act Award 2022 (equipe do Refugee Film Festival). Confirmar.
- O pop-up que o CV dela chama de "Untitled: Palestine (working title)" aparece no protótipo com o nome público usado pela HIAP: **Visible Palestine**.

## The Washington Post — "How is 'happiness' measured around the world?" (27/11/2025)

- O capítulo da Finlândia ("Life satisfaction") tem 8 fotos com crédito "Photos by Nora Sayyad/For The Washington Post". Estão na página Commissions (bloco "Selected assignments") e na lista cronológica da Current.
- **As imagens usadas são as cópias publicadas pelo jornal** (salvas da página por Robson, reduzidas para 1000×1500). Antes do site no ar: pedir os originais à Nora e confirmar que o contrato com o Washington Post permite mostrar as fotos no portfólio.
- As fotos mostram pessoas identificáveis, inclusive crianças: confirmar com a Nora.
- As ilustrações da matéria (por exemplo "Life Satisfaction") são arte do jornal e não entram no site.

