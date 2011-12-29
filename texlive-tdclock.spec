# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/tdclock
# catalog-date 2009-06-23 13:06:36 +0200
# catalog-license gpl2
# catalog-version v2.2
Name:		texlive-tdclock
Version:	v2.2
Release:	1
Summary:	A ticking digital clock package for PDF output
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tdclock
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tdclock.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tdclock.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A ticking digital clock package to be used in Pdf-LaTeX
documents, for example in presentations.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tdclock/tdclock.sty
%doc %{_texmfdistdir}/doc/latex/tdclock/README
%doc %{_texmfdistdir}/doc/latex/tdclock/tdclock-beamer-example.pdf
%doc %{_texmfdistdir}/doc/latex/tdclock/tdclock-beamer-example.tex
%doc %{_texmfdistdir}/doc/latex/tdclock/tdclock-doc.pdf
%doc %{_texmfdistdir}/doc/latex/tdclock/tdclock-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
