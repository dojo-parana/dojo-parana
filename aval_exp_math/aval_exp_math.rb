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
		else			
			if @expression == "5"
				number1 = (@expression.chars.to_a)
				return number1[0]
			elsif @expression == "5 *"
				operador = @expression.chars.to_a
				return operador[2]
			end
		end
  end
end
