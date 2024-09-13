from manim import *

class GraphSLE2(Scene):
    def construct(self):
        line1=Text("Solve System of Linear Equations")
        line2=Text("by Graphing",t2c={"Graphing":YELLOW})
        VGroup(line1, line2).arrange(DOWN, buff=1)
        ul_line1=Underline(line1,color=GREEN,sheen_factor = -0.5)
        ul_line2=Underline(line2,color=GREEN,sheen_factor = -0.5)
        self.play(Write(line1))
        self.play(Write(line2))
        self.play(GrowFromCenter(ul_line1),
                  GrowFromCenter(ul_line2),
                  ShowPassingFlashWithThinningStrokeWidth(line1),
                  ShowPassingFlashWithThinningStrokeWidth(line2),
                  run_time=0.5)
        self.play(Flash(line2[-1:-9].get_top(),color=YELLOW,line_length=5,line_stroke_width=0.5,num_lines=28))
        
        
        self.play(ShrinkToCenter(line1),ShrinkToCenter(line2),ShrinkToCenter(ul_line1),ShrinkToCenter(ul_line2))
        
        #Display Equations on the screen
        equation1 = MathTex("3x + 2y = 12", r"\quad (1)",tex_to_color_map={"3x + 2y = 12": GREEN})
        equation2 = MathTex("x - 2y = -4", r"\quad (2)",tex_to_color_map={"x - 2y = -4": BLUE})

        # Set color for the labels "(1)" and "(2)"
        equation1.set_color_by_tex("(1)", GREEN)
        equation2.set_color_by_tex("(2)", BLUE)

        # Position the equations
        equation1.to_edge(UP)
        equation2.next_to(equation1, DOWN,buff=0.5)

        # Display the equations
        self.play(Write(equation1))
        self.play(Write(equation2))

        # # Highlight the equations using SurroundingRectangle
        # self.play(Create(SurroundingRectangle(equation1[0], color=RED)))
        # self.play(Create(SurroundingRectangle(equation2[0], color=RED)))

        # Highlight only the equation part, not the labels
        rect1 = SurroundingRectangle(equation1[0], color=YELLOW)  # Exclude the label (1)
        rect2 = SurroundingRectangle(equation2[0], color=YELLOW)  # Exclude the label (2)

        
        self.play(Create(rect1))
        self.play(Create(rect2))

        step1=Text("Let's solve the equations").scale(1)
        step1.next_to(equation2,DOWN)
        self.play(Write(step1))

        # Add a flash effect to highlight the label (1) and (2)
        flash1 = Flash(equation1.get_part_by_tex("(1)"), color=GREEN, line_length=0.2)
        flash2 = Flash(equation2.get_part_by_tex("(2)"), color=BLUE, line_length=0.2)


        # Group equation1 and its surrounding rectangle
        group1 = VGroup(equation1, rect1)
        group2 = VGroup(equation2,rect2)
        

        self.play(flash1)

        # Move the group to the middle left of the screen
        # group1.to_edge(LEFT)
        

        # Animate the movement
        self.play(group1.animate.to_edge(LEFT))
        self.play(flash2)
        self.play(group2.animate.to_edge(UR))
        self.play(ShrinkToCenter(step1))


         # Create a vertical line across the screen
        line = Line(start=DOWN*8, end=UP*8, color=WHITE)
        line.set_stroke(width=1.5)
        # Display the line
        self.play(Create(line))

        # Display x-intercept of equation 1 on the screen
        eq1_x = Text("step 1: find x-intercept, put y=0",font="Arial",t2c={"x-intercept":GREEN,"y=0":YELLOW},t2s={"x-intercept": ITALIC,"y=0":ITALIC},).scale(0.5)
        self.play(eq1_x.animate.next_to(group1,DOWN))

        # Step 1: Display the original equation
        eq1_display_x = MathTex(r"3\mathbf{\mathit{x}} + 2y = 12",tex_to_color_map={"x": GREEN, "y": YELLOW}).scale(0.8)
        eq1_display_x.next_to(eq1_x,DOWN)

        x_symbol1 = eq1_display_x.get_part_by_tex("x")
        
         

        # Step 2: Show substitution y = 0
        eq1_sub_x = MathTex(r"3\mathbf{\mathit{x}} + 2(0) = 12", tex_to_color_map={"x": GREEN, "0": YELLOW}).scale(0.8)
        eq1_sub_x.next_to(eq1_display_x,DOWN)

        x_symbol2 = eq1_sub_x.get_part_by_tex("x")
        y_symbol2 = eq1_sub_x.get_part_by_tex("0")


        # Step 3: Simplify to 3x = 12
        eq1_simplified_x = MathTex("3x = 12", tex_to_color_map={"x": GREEN}).scale(0.8)
        eq1_simplified_x .next_to(eq1_sub_x, DOWN)

        x_symbol3 = eq1_simplified_x.get_part_by_tex("x")
        ul_x3=Underline(eq1_simplified_x[0:2],color=RED)

        # Step 4: Solve for x
        eq1_solution_x = MathTex("x = \\frac{12}{3} = 4", tex_to_color_map={"x": GREEN}).scale(0.8)
        eq1_solution_x.next_to(eq1_simplified_x , DOWN)
        ul_x4 = Underline(eq1_solution_x[0][0],color=RED)

        #animate x,y,0 up and down


        # Display the steps one by one
        self.play(Write(eq1_display_x))
        self.wait(1)
        self.play(Write(eq1_sub_x))
        self.play(y_symbol2.animate.shift(UP * 0.2),eq1_x[25:28].animate.shift(UP * 0.2),color=WHITE)
        self.play(y_symbol2.animate.shift(DOWN * 0.2),eq1_x[25:28].animate.shift(DOWN * 0.2))
        self.wait(1)
        self.play(Write(eq1_simplified_x ))
        self.play(Write(ul_x3),run_time=0.5)
        self.play(x_symbol3.animate.shift(UP * 0.3))
        self.play(x_symbol3.animate.shift(DOWN * 0.3))
        self.wait(1)
        
        self.play(ReplacementTransform(ul_x3,ul_x4),run_time=1)
        self.play(Write(eq1_solution_x))
        self.wait(1)

        

        # Highlight the x-intercept
        eq1_x_intercept = Text("x-intercept = (4,0)", color=GREEN,t2s={"x-intercept = (4,0)": ITALIC}).scale(0.8)
        eq1_x_intercept.next_to(eq1_solution_x, DOWN)
        self.play(Write(eq1_x_intercept))
        self.wait(1)

        eq1_x_group =VGroup(eq1_display_x,eq1_sub_x,eq1_simplified_x,eq1_solution_x,ul_x3,ul_x4)
        self.play(FadeOut(eq1_x_group))
        eq1_x_intercept.next_to(eq1_x,DOWN).scale(0.8)
        self.play(Write(eq1_x_intercept))
        self.wait(1)

        # Display y-intercept of equation 1 on the screen
        eq1_y = Text("step 2: find y-intercept, put x=0",font="Arial",t2c={"y-intercept":GREEN,"x=0":YELLOW},t2s={"y-intercept": ITALIC,"x=0":ITALIC},).scale(0.5)
        self.play(eq1_y.animate.next_to(eq1_x_intercept,DOWN))

        # Step 1: Display the original equation
        eq1_display_y = MathTex(r"3\mathbf{\mathit{x}} + 2y = 12",tex_to_color_map={"x": YELLOW, "y": GREEN}).scale(0.8)
        eq1_display_y.next_to(eq1_y,DOWN)

        y_symbol1 = eq1_display_x.get_part_by_tex("y")
        
         

        # Step 2: Show substitution x = 0
        eq1_sub_y = MathTex(r"3(0) + 2\mathbf{\mathit{y}}= 12", tex_to_color_map={"0": YELLOW, "y": GREEN}).scale(0.8)
        eq1_sub_y.next_to(eq1_display_y,DOWN)

        x_symbol2 = eq1_sub_y.get_part_by_tex("0")
        y_symbol2 = eq1_sub_y.get_part_by_tex("y")


        # Step 3: Simplify to 2y = 12
        eq1_simplified_y = MathTex("2y = 12", tex_to_color_map={"y": GREEN}).scale(0.8)
        eq1_simplified_y .next_to(eq1_sub_y, DOWN)

        y_symbol3 = eq1_simplified_y.get_part_by_tex("y")
        ul_y3=Underline(eq1_simplified_y[0:2],color=RED)

        # Step 4: Solve for y
        eq1_solution_y = MathTex("y = \\frac{12}{2} = 6", tex_to_color_map={"y": GREEN}).scale(0.8)
        eq1_solution_y.next_to(eq1_simplified_y , DOWN)
        ul_y4 = Underline(eq1_solution_y[0][0],color=RED)

        
        # Display the steps one by one
        self.play(Write(eq1_display_y))
        self.wait(1)
        self.play(Write(eq1_sub_y))
        self.play(x_symbol2.animate.shift(UP * 0.2),eq1_y[25:28].animate.shift(UP * 0.2),color=WHITE)
        self.play(x_symbol2.animate.shift(DOWN * 0.2),eq1_y[25:28].animate.shift(DOWN * 0.2))
        self.wait(1)
        self.play(Write(eq1_simplified_y ))
        self.play(Write(ul_y3),run_time=0.5)
        self.play(y_symbol3.animate.shift(UP * 0.3))
        self.play(y_symbol3.animate.shift(DOWN * 0.3))
        self.wait(1)
        
        self.play(ReplacementTransform(ul_y3,ul_y4),run_time=1)
        self.play(Write(eq1_solution_y))
        self.wait(1)

        # Highlight the y-intercept
        eq1_y_intercept = Text("y-intercept = (0,6)", color=GREEN,t2s={"y-intercept = (0,6)": ITALIC}).scale(0.8)
        eq1_y_intercept.next_to(eq1_solution_y, DOWN)
        self.play(Write(eq1_y_intercept))
        self.wait(1)

        eq1_y_group =VGroup(eq1_display_y,eq1_sub_y,eq1_simplified_y,eq1_solution_y,ul_y3,ul_y4)
        self.play(FadeOut(eq1_y_group))
        eq1_y_intercept.next_to(eq1_y,DOWN).scale(0.8)
        self.play(Write(eq1_y_intercept))
        self.wait(1)



        # Display x-intercept of equation 2 on the screen
        eq2_x = Text("step 1: find x-intercept, put y=0",font="Arial",t2c={"x-intercept":BLUE,"y=0":YELLOW},t2s={"x-intercept": ITALIC,"y=0":ITALIC},).scale(0.5)
        self.play(eq2_x.animate.next_to(group2,DOWN))

        # Step 1: Display the original equation
        eq2_display_x = MathTex(r"\mathbf{\mathit{x}} - 2y = -4",tex_to_color_map={"x": BLUE, "y": YELLOW}).scale(0.8)
        eq2_display_x.next_to(eq2_x,DOWN)

        x_symbol1 = eq2_display_x.get_part_by_tex("x")
        
         

        # Step 2: Show substitution y = 0
        eq2_sub_x = MathTex(r"\mathbf{\mathit{x}} - 2(0) = -4", tex_to_color_map={"x": BLUE, "0": YELLOW}).scale(0.8)
        eq2_sub_x.next_to(eq2_display_x,DOWN)

        x_symbol2 = eq2_sub_x.get_part_by_tex("x")
        y_symbol2 = eq2_sub_x.get_part_by_tex("0")


        # Step 4: Solve for x
        eq2_solution_x = MathTex("x = - 4", tex_to_color_map={"x": BLUE}).scale(0.8)
        eq2_solution_x.next_to(eq2_sub_x , DOWN)
        ul_x4 = Underline(eq2_solution_x[0][0],color=RED)

        


        # Display the steps one by one
        self.play(Write(eq2_display_x))
        self.wait(1)
        self.play(Write(eq2_sub_x))
        self.play(y_symbol2.animate.shift(UP * 0.2),eq2_x[25:28].animate.shift(UP * 0.2),color=WHITE)
        self.play(y_symbol2.animate.shift(DOWN * 0.2),eq2_x[25:28].animate.shift(DOWN * 0.2))
        self.wait(1)
        # self.play(x_symbol2.animate.shift(UP * 0.3))
        # self.play(x_symbol2.animate.shift(DOWN * 0.3))
        self.wait(1)
        
        
        self.play(Write(eq2_solution_x))
        self.play(Write(ul_x4))
        self.wait(1)


        # Highlight the x-intercept
        eq2_x_intercept = Text("x-intercept = (-4,0)", color = BLUE,t2s={"x-intercept = (-4,0)": ITALIC}).scale(0.8)
        eq2_x_intercept.next_to(eq2_solution_x, DOWN)
        self.play(Write(eq2_x_intercept))
        self.wait(1)

        eq2_x_group =VGroup(eq2_display_x,eq2_sub_x,eq2_solution_x,ul_x4)
        self.play(FadeOut(eq2_x_group))
        eq2_x_intercept.next_to(eq2_x,DOWN).scale(0.8)
        self.play(Write(eq2_x_intercept))
        self.wait(1)

         # Display y-intercept of equation 2 on the screen
        eq2_y = Text("step 2: find y-intercept, put x=0",font="Arial",t2c={"y-intercept":BLUE,"x=0":YELLOW},t2s={"y-intercept": ITALIC,"x=0":ITALIC},).scale(0.5)
        self.play(eq2_y.animate.next_to(eq2_x_intercept,DOWN))

        # Step 1: Display the original equation
        eq2_display_y = MathTex(r"\mathbf{\mathit{x}} - 2y = -4",tex_to_color_map={"x": YELLOW, "y": BLUE}).scale(0.8)
        eq2_display_y.next_to(eq2_y,DOWN)

        y_symbol1 = eq1_display_x.get_part_by_tex("y")
        
         

        # Step 2: Show substitution x = 0
        eq2_sub_y = MathTex(r"(0) - 2\mathbf{\mathit{y}}= -4", tex_to_color_map={"0": YELLOW, "y": BLUE}).scale(0.8)
        eq2_sub_y.next_to(eq2_display_y,DOWN)

        x_symbol2 = eq2_sub_y.get_part_by_tex("0")
        y_symbol2 = eq2_sub_y.get_part_by_tex("y")

        # Step 3: Simplify to 2y = 4
        eq2_simplified_y = MathTex("2y = 4", tex_to_color_map={"y": BLUE}).scale(0.8)
        eq2_simplified_y.next_to(eq2_sub_y, DOWN)

        y_symbol3 = eq2_simplified_y.get_part_by_tex("y")
        ul_y3=Underline(eq2_simplified_y[0:2],color=RED)

        # Step 4: Solve for y
        eq2_solution_y = MathTex("y = \\frac{4}{2} = 2", tex_to_color_map={"y": BLUE}).scale(0.8)
        eq2_solution_y.next_to(eq2_simplified_y , DOWN)
        ul_y4 = Underline(eq2_solution_y[0][0],color=RED)

        #animate x,y,0 up and down


        # Display the steps one by one
        self.play(Write(eq2_display_y))
        self.wait(1)
        self.play(Write(eq2_sub_y))
        self.play(x_symbol2.animate.shift(UP * 0.2),eq2_y[25:28].animate.shift(UP * 0.2),color=WHITE)
        self.play(x_symbol2.animate.shift(DOWN * 0.2),eq2_y[25:28].animate.shift(DOWN * 0.2))
        self.wait(1)
        self.play(Write(eq2_simplified_y ))
        self.play(Write(ul_y3),run_time=0.5)
        self.play(y_symbol3.animate.shift(UP * 0.3))
        self.play(y_symbol3.animate.shift(DOWN * 0.3))
        self.wait(1)
        
        self.play(ReplacementTransform(ul_y3,ul_y4),run_time=1)
        self.play(Write(eq2_solution_y))
        self.wait(1)

        # Highlight the y-intercept
        eq2_y_intercept = Text("y-intercept = (0,2)", color = BLUE,t2s={"y-intercept = (0,2)": ITALIC}).scale(0.8)
        eq2_y_intercept.next_to(eq2_solution_y, DOWN)
        self.play(Write(eq2_y_intercept))
        self.wait(1)

        eq2_y_group =VGroup(eq2_display_y,eq2_sub_y,eq2_simplified_y,eq2_solution_y,ul_y3,ul_y4)
        self.play(FadeOut(eq2_y_group))
        eq2_y_intercept.next_to(eq2_y,DOWN).scale(0.8)
        self.play(Write(eq2_y_intercept))
        self.wait(1)

        stepObjects=VGroup(eq1_x,eq1_y,eq2_x,eq2_y)
        self.play(FadeOut(stepObjects))
        self.play(eq1_x_intercept.animate.next_to(group1,DOWN))
        self.play(eq1_y_intercept.animate.next_to(eq1_x_intercept,DOWN))
        self.play(eq2_x_intercept.animate.next_to(group2,DOWN))
        self.play(eq2_y_intercept.animate.next_to(eq2_x_intercept,DOWN),ShrinkToCenter(line))
        self.wait(1)

        step3=Text("Plot points on the graph and draw the lines").scale(0.5)
        step3.shift(ORIGIN)
        self.play(step3.animate.to_edge(DOWN))

        
        # Create Axes
        axes = Axes(
            x_range=[-6, 6],  # x-axis from -6 to 6
            y_range=[-8, 8],  # y-axis from -6 to 6
            
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
                
            },
            
            y_axis_config={
                "include_tip": True,
            }
        )
        axes.set_height(12)
        axes.set_width(12)

        # Add coordinate labels
        axes.add_coordinates(
             font_size=20,
            num_decimal_places=1,
        )

        # Add labels for the axes
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Equation 1: 3x + 2y = 12 -> y =-1.5 * x + 6
        eq1_graph = axes.plot(lambda x: -1.5 * x + 6, color=GREEN, x_range=[-6, 6])
        # eq1_label = MathTex("3x + 2y = 12").next_to(eq1_graph, RIGHT)

        # Equation 2: x - 2y = -4 -> y = (x + 4) / 2
        eq2_graph = axes.plot(lambda x: (x + 4) / 2, color=BLUE, x_range=[-6, 6])
        # eq2_label = MathTex("x - 2y = -4").next_to(eq2_graph, RIGHT)

        # Mark x and y intercepts for Equation 1 (3x + 2y = 12)
        x_intercept_eq1 = Dot(axes.coords_to_point(4, 0), color=PINK)
        y_intercept_eq1 = Dot(axes.coords_to_point(0, 6), color=PINK)
        x_label_eq1 = MathTex("(4, 0)").next_to(x_intercept_eq1, DOWN)
        y_label_eq1 = MathTex("(0, 6)").next_to(y_intercept_eq1, LEFT)

        # Mark x and y intercepts for Equation 2 (x - 2y = -4)
        x_intercept_eq2 = Dot(axes.coords_to_point(-4, 0), color=TEAL)
        y_intercept_eq2 = Dot(axes.coords_to_point(0, 2), color=TEAL)
        x_label_eq2 = MathTex("(-4, 0)").next_to(x_intercept_eq2, DOWN)
        y_label_eq2 = MathTex("(0, 2)").next_to(y_intercept_eq2, LEFT)


        # Mark the intercepts for both equations (optional)
        # Mark the solution of both equations (2, 3)
        solution = Dot(axes.coords_to_point(2, 3), color=ORANGE)
        solution_label = MathTex(r"(2, 3)").next_to(solution, UP)


        # Create dotted lines from the solution point to the x-axis and y-axis
        x_dotted_line = DashedLine(
            start=solution, 
            end=axes.c2p(2, 0),
            color=YELLOW
        )
        y_dotted_line = DashedLine(
            start=solution, 
            end=axes.c2p(0, 3),
            color=YELLOW
        )

        intercept_labels=VGroup(labels,x_label_eq1,y_label_eq1,x_label_eq2,y_label_eq2,step3,group1,group2)
        shrink_params=VGroup(axes,x_intercept_eq1,y_intercept_eq1,x_intercept_eq2,y_intercept_eq2,eq1_x_intercept,eq1_y_intercept,eq2_x_intercept,eq2_y_intercept,eq1_graph,eq2_graph,solution,solution_label,x_dotted_line,y_dotted_line)

        # Display everything on the screen
        self.play(Create(axes), Write(labels))

        # Display Equation 1 and its intercepts
        self.play(FadeIn(x_intercept_eq1), ReplacementTransform(eq1_x_intercept,x_label_eq1),run_time=1)
        self.play(Indicate(x_label_eq1,color=GOLD_E),Indicate(x_intercept_eq1))
        self.play(FadeIn(y_intercept_eq1), ReplacementTransform(eq1_y_intercept,y_label_eq1),run_time=1)
        self.play(Indicate(y_label_eq1,color=GOLD_E),Indicate(y_intercept_eq1))
        self.play(Create(eq1_graph),run_time=2)

        # Display Equation 2 and its intercepts
        self.play(FadeIn(x_intercept_eq2), ReplacementTransform(eq2_x_intercept,x_label_eq2),run_time=1)
        self.play(Indicate(x_label_eq2,color=GOLD_A),Indicate(x_intercept_eq2))
        self.play(FadeIn(y_intercept_eq2), ReplacementTransform(eq2_y_intercept,y_label_eq2),run_time=1)
        self.play(Indicate(y_label_eq2,color=GOLD_A),Indicate(y_intercept_eq2))
        self.play(Create(eq2_graph),run_time=2)

        # Mark the solution point (2, 3)
        self.play(Create(x_dotted_line), Create(y_dotted_line))
        self.play(Indicate(solution),Write(solution_label))
        self.play(FadeOut(intercept_labels))
        self.wait(2)
        self.play(ShrinkToCenter(shrink_params))

        #Display result
        result=Text("The intersection (2,3) is the solution to the system of equation",t2c={"(2,3)":YELLOW,"solution to the system of equation":GOLD}).scale(0.5)
        self.play(Write(result))
        self.play(ShowPassingFlashWithThinningStrokeWidth(result),run_time=1)
        self.wait(2)

        #Display Thank you message
        tk=Text("Thank You!!!",color=BLUE)
        name=Text("by Rari",color=TEAL)
        name.next_to(tk,DR)
        self.play(FadeOut(result))
        self.play(FadeIn(tk))
        self.play(Write(name),run_time=1)
        self.wait(1)
        
        






       