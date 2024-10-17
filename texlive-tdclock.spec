Name:		texlive-tdclock
Version:	33043
Release:	2
Summary:	A ticking digital clock package for PDF output
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tdclock
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tdclock.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tdclock.doc.r%{version}.tar.xz
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
%doc %{_texmfdistdir}/doc/latex/tdclock/Changelog
%doc %{_texmfdistdir}/doc/latex/tdclock/README
%doc %{_texmfdistdir}/doc/latex/tdclock/tdclock-beamer-example.pdf
%doc %{_texmfdistdir}/doc/latex/tdclock/tdclock-beamer-example.tex
%doc %{_texmfdistdir}/doc/latex/tdclock/tdclock-doc.pdf
%doc %{_texmfdistdir}/doc/latex/tdclock/tdclock-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
