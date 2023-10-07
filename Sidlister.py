import sublist3r
from subprocess import Popen, PIPE
import pyfiglet  # Import the pyfiglet library
import sys  # Import the sys module for exit

def show_intro():
    # Create ASCII art for "Tool By Siddharth Kumar" with smaller font size and red color
    intro_message = pyfiglet.figlet_format("Tool By Siddharth Kumar", font="mini", justify="center")
    intro_message = f"\033[91m{intro_message}\033[0m"  # Add red color

    # Use cowsay and fortune to display a fun introduction
    p1 = Popen(["fortune"], stdout=PIPE)
    p2 = Popen(["cowsay", "-f", "dragon"], stdin=p1.stdout, stdout=PIPE)
    p1.stdout.close()
    output = p2.communicate()[0]
    print(output.decode("utf-8"))
    print(intro_message)  # Display the ASCII art

def save_to_html(subdomains, output_file):
    sorted_subdomains = sorted(subdomains)  # Sort the subdomains alphabetically
    with open(output_file, 'w') as file:
        file.write("<html><head><title>Subdomain Enumeration Results</title>")
        file.write('<style>'
                   'body { background-color: #f0f0f0; font-family: Arial, sans-serif; }'
                   'h1 { color: #333; }'
                   'p { font-style: italic; }'
                   'ul { list-style-type: circle; }'
                   'li { color: #007bff; }'
                   '</style>')
        file.write("</head><body>")
        file.write("<h1>Sidlister's Subdomain Enumeration Results</h1>")
        file.write("<p>Tool by Siddharth Kumar</p>")
        file.write("<ul>")
        for subdomain in sorted_subdomains:
            file.write(f'<li>{subdomain}</li>')
        file.write("</ul>")
        file.write("</body></html>")
    print(f"Results saved to {output_file}")

def main():
    try:
        show_intro()  # Display the 3D intro
        domain = input("Enter the domain name without protocol names (http/https)-: ")
        output_file = "mephisto_results.html"

        # Use Sublist3r to enumerate subdomains
        subdomains = sublist3r.main(domain, 40, None, None, False, False, False, None)

        # Save the results to an HTML file with sorted and styled subdomains
        save_to_html(subdomains, output_file)

    except KeyboardInterrupt:  # Catch Ctrl+C
        print("\033[91mGoodbye\033[0m")  # Display "Goodbye" in red color
        sys.exit(0)  # Exit the program gracefully

if __name__ == "__main__":
    main()
