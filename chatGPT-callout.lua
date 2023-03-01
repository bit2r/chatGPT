local h2 = pandoc.Header(2, "chatGPT 답변: ")

function Div(el)
if quarto.doc.isFormat("html") then
if el.classes:includes('chatGPT-callout-tip') then
local content = el.content
table.insert(content, 1, h2)
return pandoc.Div(
  content,
  {class="callout-tip", collapse='true'}
)
end
end
end
