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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A ticking digital clock package to be used in Pdf-LaTeX
documents, for example in presentations.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tdclock/tdclock.sty
%doc %{_texmfdistdir}/doc/latex/tdclock/README
%doc %{_texmfdistdir}/doc/latex/tdclock/tdclock-beamer-example.pdf
%doc %{_texmfdistdir}/doc/latex/tdclock/tdclock-beamer-example.tex
%doc %{_texmfdistdir}/doc/latex/tdclock/tdclock-doc.pdf
%doc %{_texmfdistdir}/doc/latex/tdclock/tdclock-doc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
