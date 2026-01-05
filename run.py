#!/usr/bin/env python3
"""
Resume Builder - Application Entry Point

Run this file to start the Flask development server.

Usage:
    python run.py                    # Start with default resume
    python run.py --debug            # Start in debug mode
    python run.py --port 8080        # Start on custom port

For custom resume data:
    from my_resume import resume_data
    import app
    app.create_app(resume_data).run()
"""

import os
import argparse
import app


def main():
    """Main entry point for the Resume Builder application."""
    parser = argparse.ArgumentParser(
        description='Resume Builder - A Flask-powered resume/CV web application'
    )
    parser.add_argument(
        '--debug', '-d',
        action='store_true',
        help='Run in debug mode with auto-reload'
    )
    parser.add_argument(
        '--port', '-p',
        type=int,
        default=5010,
        help='Port to run the server on (default: 5000)'
    )
    parser.add_argument(
        '--host', '-H',
        type=str,
        default='127.0.0.1',
        help='Host to bind to (default: 127.0.0.1, use 0.0.0.0 for public)'
    )
    
    args = parser.parse_args()
    
    # Check for FLASK_DEBUG environment variable
    debug = args.debug or os.environ.get('FLASK_DEBUG', '0') == '1'
    
    # Create and run the application
    application = app.create_app()
    
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║                    📄 Resume Builder                         ║
╠══════════════════════════════════════════════════════════════╣
║  Server running at: http://{args.host}:{args.port:<5}                    ║
║  Debug mode: {'ON ' if debug else 'OFF'}                                           ║
║  Press CTRL+C to quit                                        ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    application.run(
        host=args.host,
        port=args.port,
        debug=debug
    )


if __name__ == '__main__':
    main()
