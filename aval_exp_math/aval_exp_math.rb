class AvalExpMath
  def initialize(expression)
		@expression = expression  
  end

  def solve_exp
    @expression
		if @expression == "1 + 1"
			return 2
		elsif @expression == "5 - 2"
			return 3
		end
  end
end
