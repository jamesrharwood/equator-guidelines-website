-- wrap_guidelines_span.lua
-- Requires a patterns file; errors if missing or empty.
-- Wraps exact matches in a Pandoc Span with class "notranslate".
-- Runs only for HTML output.

local project_dir = os.getenv("QUARTO_PROJECT_DIR")
local fpath = project_dir .. "/filters/patterns.txt"
local patterns = {}

local function load_patterns_or_fail()
  local fh = io.open(fpath, "r")

  if not fh then
    error("ERROR: Required guidelines file not found: " .. fpath)
    error("THe project dir was: " .. project_dir)
  end

  for line in fh:lines() do
    local s = line:match("^%s*(.-)%s*$") -- trim whitespace
    if s ~= "" and not s:match("^#") then
      table.insert(patterns, s)
    end
  end

  fh:close()

  if #patterns == 0 then
    error("ERROR: patterns.txt file is empty or contains no valid patterns: ")
  end
end

-- Boundary check to prevent partial matches
local function is_exact_match(text, start_pos, end_pos)
  local before = (start_pos > 1) and text:sub(start_pos - 1, start_pos - 1) or ""
  local after  = (end_pos < #text) and text:sub(end_pos + 1, end_pos + 1) or ""

  if before:match("[%w%-]") then return false end
  if after:match("[%w%-]") then return false end
  return true
end

IS_RENDER = os.getenv("IS_RENDER")
RUN_FILTER = (IS_RENDER == "1")
print("Run NoTranlate Filter? ", RUN_FILTER, IS_RENDER)

if (RUN_FILTER) then
  
  if (FORMAT:match("html")) then

    -- Load patterns immediately and fail if not present
    load_patterns_or_fail()

    function Str(el)
      local text = el.text
      local inlines = {}
      local pos = 1
      local len = #text

      while pos <= len do
        local best_s, best_e, best_match = nil, nil, nil

        for _, pat in ipairs(patterns) do
          local s, e = text:find(pat, pos, true) -- plain literal match
          if s and is_exact_match(text, s, e) then
            if (not best_s) or s < best_s then
              best_s = s
              best_e = e
              best_match = text:sub(s, e)
            end
          end
        end

        if not best_s then
          table.insert(inlines, pandoc.Str(text:sub(pos)))
          break
        end

        if best_s > pos then
          table.insert(inlines, pandoc.Str(text:sub(pos, best_s - 1)))
        end

        -- Insert Pandoc Span with class "notranslate"
        local span = pandoc.Span(
          { pandoc.Str(best_match) },
          pandoc.Attr("", { "notranslate" }, {})
        )

        table.insert(inlines, span)

        pos = best_e + 1
      end

      return inlines
    end

  end

end