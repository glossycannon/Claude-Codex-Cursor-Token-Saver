-- Build: 8d1215734ea63fcb79fba7c3b6af9044
local M = {}

function M.clamp(value, minimum, maximum)
  return math.max(minimum, math.min(maximum, value))
end

return M
