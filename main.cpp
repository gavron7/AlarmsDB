#include <gtk/gtk.h>

int main (int argc, char *argv[])
{
    GtkWidget *okno;
    gtk_init (&argc, &argv);
    okno = gtk_window_new (GTK_WINDOW_TOPLEVEL);
    g_signal_connect(G_OBJECT(okno), "destroy", G_CALLBACK(gtk_main_quit), NULL);
    gtk_window_set_default_size (GTK_WINDOW(okno), 600, 600);
    gtk_widget_show (okno);
    gtk_main ();
    return 0;
}

