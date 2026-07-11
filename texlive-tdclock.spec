%global tl_name tdclock
%global tl_revision 33043

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.5
Release:	%{tl_revision}.1
Summary:	A ticking digital clock package for PDF output
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tdclock
License:	gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tdclock.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tdclock.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A ticking digital clock package to be used in Pdf-LaTeX documents, for
example in presentations.

